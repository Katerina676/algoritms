# --- ПРИНЦИП РАБОТЫ ---
# Реализация бинарного дерева поиска. Сначало мы рекурсивно ищем искомый элемент ,который нужно удалить, потом проверяем
# есть ли у него листья и ищем там элемент на замену удаленному.
# --- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ ---
# На вход подается именно бинарное дерево поэтому мы можем быть уверены что с помощью данного алгоритма
# если мы удалим элемент,и найдем элемент ему
# на замену дерево не распадется.
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
# Дерево является деревом поиска где сложность прохода по нему будет состовлять O(H) , где H-высота дерева
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
# Требуется O(n) памяти , где n количество элементов которые хранятся в дереве.

# id 64557704
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def remove(root, key):
    if root is None:
        return root
    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        node = root.right
        while node.left is not None:
            node = node.left
        root.value = node.value
        root.right = remove(root.right, node.value)
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


print(test())
