# --- ПРИНЦИП РАБОТЫ ---
# Реализация бинарного дерева поиска. Происходит поиск нужного элемента, который нужно удалить, и его родителя,
# по ключу. Потом определяется является ли искомый элемент корнем или нет и в зависимости от этого подбираются
# дальнейшие действия, а именно поиск в поддереве искомого элемента самый нижний правый у которого нет детей,
# если элемента нет то возвращаем None, искомый элемент удаляем из дерева и вставляем на место того что нам нужно
# удалить.
# --- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ ---
# На вход подается именно бинарное дерево поэтому мы можем быть уверены что с помощью данного алгоритма
# если мы удалим элемент,и найдем элемент ему на замену дерево не распадется потому что если у элемента который мы
# должны удалить нет потомков, то присваем ему значение None, если нет левого потомка, но есть правый, то выясним
# наш элемент был правым или левым по отношению к родителю и в зависимости от этого соединим правого потомка с родителем
# элемента, если у элемента оба потомка есть, то мы запустим поиск в левой вершине потомка правого поддерева и найдем
# нижний правый элемент, сохраним его и присвоим ему значение None и потом вставим его на место того что мы удалили,
# чтобы вершины не распались,если наш элемент это начальная вершина,то проверим если у него нет потомков то удалим
# вершину, если у нее нет левого потомка,то переместим вершину в правого потомка, если есть оба потомка или только левый
# то запустим поиск в левом потомке в правом поддереве и найдем нижнего правового присвоем ему None и удаленному
# элементу присвоим значение найденного.
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
# Дерево является деревом поиска где сложность прохода по нему будет состовлять O(H) , где H-высота дерева
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
# Требуется O(n) памяти , где n количество элементов которые хранятся в дереве.

# id 64557774
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def search_target(root, key, parent):
    if root is None:
        return None, None
    if root.value == key:
        return root, parent
    if root.value > key:
        return search_target(root.left, key, root)
    else:
        return search_target(root.right, key, root)


def search_node(root):
    if root.right is None:
        return root

    while root.right:
        if root.right.right is None:
            target = root.right
            root.right = None
            return target

        root = root.right


def remove(root, key):
    if root is None:
        return root

    node, node_parent = search_target(root, key, None)
    if node is None:
        return root

    if node is root:
        if node.left is None and node.right is None:
            root = None
            return root

        elif node.left is None:
            root = node.right
        else:
            searched = search_node(node.left)
            root = searched

            if searched is not node.left:
                searched.left = node.left
            searched.right = node.right

        return root

    if node.left is None:
        if node.right is None:
            if node_parent.left is node:
                node_parent.left = None
            else:
                node_parent.right = None
            return root

        elif node_parent.left is node:
            node_parent.left = node.right
        else:
            node_parent.right = node.right
    else:
        searched = search_node(node.left)
        if node_parent.left is node:
            node_parent.left = searched
        else:
            node_parent.right = searched

        if searched is not node.left:
            searched.left = node.left

        searched.right = node.right

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
