class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # --- Daraxtga element qo'shish ---
    def insert(self, data):
        if self.root is None:
            self.root = BinaryTreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    # --- Element qidirish ---
    def search(self, node, key):
        if node is None or node.data == key:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def search_value(self, key):
        return self.search(self.root, key)

    # --- Eng kichik element ---
    def find_min(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.data

    # --- Eng katta element ---
    def find_max(self, node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.data

# --- Misol ishlatish ---
if __name__ == "__main__":
    bst = BinarySearchTree()
    for x in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(x)

    print("Eng kichik:", bst.find_min(bst.root))
    print("Eng katta:", bst.find_max(bst.root))

    key = 40
    result = bst.search_value(key)
    if result:
        print(f"{key} topildi")
    else:
        print(f"{key} topilmadi")