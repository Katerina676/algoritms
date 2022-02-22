class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root) -> bool:
    if root is None:
        return True
    if root.left is not None:
        if root.value <= root.left.value:
            return False

    if root.right is not None:
        if root.value >= root.right.value:
            return False

    return solution(root.left) and solution(root.right)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    assert solution(node5)
    node2.value = 2
    assert not solution(node5)


print(test())
