class Node:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right


def n_largest_ordered_bt(node: Node, n: int) -> int:
    array = []

    def dfs(node: Node):
        if node is None:
            return
        if not node.left and not node.right:
            array.append(node.val)
            return

        if node.left and node.right:
            dfs(node.left)
            array.append(node.val)
            dfs(node.right)
        if node.left:
            dfs(node.left)
            array.append(node.val)
        else:
            array.append(node.val)
            dfs(node.right)

    return array
