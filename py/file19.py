"""19-vazifa: Huffman kodlash va dekodlash (kod daraxtini saqlagan holda).

Matnni Huffman usuli bilan kodlaydi va qayta dekodlaydi.
"""

import heapq
from collections import Counter


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    """Huffman daraxtini quradi."""
    freq = Counter(text)
    heap = [HuffmanNode(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        node = heapq.heappop(heap)
        root = HuffmanNode(None, node.freq)
        root.left = node
        return root

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(node, prefix="", code_map=None):
    """Daraxtdan har bir belgi uchun kodlarni oladi."""
    if code_map is None:
        code_map = {}

    if node.char is not None:
        code_map[node.char] = prefix if prefix else "0"
        return code_map

    if node.left:
        build_codes(node.left, prefix + "0", code_map)
    if node.right:
        build_codes(node.right, prefix + "1", code_map)

    return code_map


def huffman_encode(text):
    """Matnni Huffman usuli bilan kodlaydi."""
    tree = build_huffman_tree(text)
    codes = build_codes(tree)
    encoded = "".join(codes[ch] for ch in text)
    return encoded, tree, codes


def huffman_decode(encoded, tree):
    """Kodlangan satrni Huffman daraxti yordamida dekodlaydi."""
    decoded = []
    node = tree

    for bit in encoded:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded.append(node.char)
            node = tree

    return "".join(decoded)


if __name__ == "__main__":
    text = "huffman kodlash algoritmi ishlaydi"
    print(f"Asl matn:     {text}")
    print(f"Asl hajmi:    {len(text) * 8} bit\n")

    encoded, tree, codes = huffman_encode(text)

    print("Huffman kodlari:")
    for char, code in sorted(codes.items()):
        display = repr(char) if char == " " else char
        print(f"  {display}: {code}")

    print(f"\nKodlangan:    {encoded}")
    print(f"Kodlangan hajmi: {len(encoded)} bit")

    decoded = huffman_decode(encoded, tree)
    print(f"\nDekodlangan:  {decoded}")
    print(f"To'g'ri dekodlandi: {decoded == text}")

    ratio = len(encoded) / (len(text) * 8) * 100
    print(f"Siqish darajasi: {ratio:.1f}%")
