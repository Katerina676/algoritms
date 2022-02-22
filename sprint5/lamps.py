class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    root_max = root.value
    if root.left is None and root.right is None:
        return root_max

    if root.left is not None:
        max_left = solution(root.left)
        if root_max < max_left:
            root_max = max_left

    if root.right is not None:
        max_right = solution(root.right)
        if root_max < max_right:
            root_max = max_right

    return root_max


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


print(test())
