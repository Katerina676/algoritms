class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    if root is None:
        return True
    left = depth_len(root.left)
    right = depth_len(root.right)
    diff = abs(left - right)
    if diff > 1:
        return False
    if solution(root.right) is True:
        return True
    if solution(root.left) is True:
        return True
    return False


def depth_len(root):
    if root is None:
        return 0
    return max(depth_len(root.left), depth_len(root.right) + 1)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


print(test())
