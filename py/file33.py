# 3. Daraxt yig‘indisini hisoblash
def tree_sum(node):
    if node is None:
        return 0
    return node.data + tree_sum(node.left) + tree_sum(node.right)