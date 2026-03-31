"""7-vazifa: bog'langan ro'yxat uchun birlashtirish saralash."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_sorted_lists(left, right):
    dummy = Node(0)
    tail = dummy

    while left and right:
        if left.value <= right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right
    return dummy.next


def split_list(head):
    if head is None or head.next is None:
        return head, None

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None
    return head, middle


def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    left, right = split_list(head)
    left_sorted = merge_sort_linked_list(left)
    right_sorted = merge_sort_linked_list(right)
    return merge_sorted_lists(left_sorted, right_sorted)


def build_linked_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


if __name__ == "__main__":
    head = build_linked_list([4, 2, 1, 3, 7, 5])
    sorted_head = merge_sort_linked_list(head)
    print("Saralangan bog'langan ro'yxat:", to_list(sorted_head))