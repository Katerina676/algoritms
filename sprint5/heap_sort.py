# --- ПРИНЦИП РАБОТЫ ---
# Из входных данных собираем кучу.Поочередно сравниваем элементы массива с левым и правым потомком,тк элемент в вершине
# должен быть не меньше элементов потомков. После того как мы привели массив к бинарной куче, мы будем "извлекать"
# по одному элементу из массива меняя их местами с самым приоритетным элементом, на каждой итерации
# снова просеивая кучу. В итоге массив получится отсортирован.
# --- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ ---
# Процедура сортировки вызывает себя рекурсивно для создания кучи сверху вниз.Мы будем искать самый большой элемент в
# массиве и ставить его в конец, итерация будет повторяться пока не останется один элемент,который будет являться
# самым маленьким.
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
# Сложность алгоритма O(n log n) в лучшем,среднем и худшем случае.
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
# Алгоритм занимает O(log n) пространства так как хранит в себе индексы в стеке вызовов.

# id 64586308

def sift_down(arr, n, idx):

    left = 2 * idx + 1
    right = 2 * idx + 2
    index_largest = idx
    for i in (left, right):
        if i < n and arr[i] > arr[index_largest]:
            index_largest = i

    if idx != index_largest:
        arr[index_largest], arr[idx] = arr[idx], arr[index_largest]
        sift_down(arr, n, index_largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        sift_down(arr, i, 0)
    return arr


def main():
    n = int(input())
    people = []
    for _ in range(n):
        name, score, penalty = input().split()
        people.append((-int(score), int(penalty), name))
    heap_sort(people)
    for i in people:
        print(i[2])


if __name__ == '__main__':
    main()
