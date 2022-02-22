class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def solution(node, idx):
    if idx == 0:
        return node.next_item
    count = 0
    head = node
    while node.next_item is not None:
        if count + 1 == idx:
            node.next_item = node.next_item.next_item
            return head
        count += 1
        node = node.next_item

    return head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    print(new_head)


print(test())