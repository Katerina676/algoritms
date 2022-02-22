# --- ПРИНЦИП РАБОТЫ ---
# Из входных данных собираем ,бинарную кучу.По очереди добавляем элементы в массив с помощью алгоритма просеивания
# вверх.После вставки проходим по массиву алгоритмом просеивания вниз формируя результат.
# --- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ ---
# Куча представляет собой очередь с приоритетом и приоритет высчитывается с помощью компаратора по условию задачи.
# Поэтому по итогу получается отсортированный массив.
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
# Сложность алгоритма O(n log n) в лучшем,среднем и худшем случае.
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
# Алгоритм занимает O(n) где n-длинна массива.

# id 64571251
def sift_up(heap, idx):
    if idx == 1:
        return idx
    parent = idx // 2
    if heap[parent] > heap[idx]:
        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = sift_up(heap, parent)
    return idx


def sift_down(heap, idx):
    length_heap = len(heap) - 1
    left = 2 * idx
    right = 2 * idx + 1
    if left > length_heap:
        return idx
    if right <= length_heap and heap[left] > heap[right]:
        index_largest = right
    else:
        index_largest = left

    if heap[index_largest] < heap[idx]:
        heap[index_largest], heap[idx] = heap[idx], heap[index_largest]
        idx = sift_down(heap, index_largest)
    return idx


def main():
    n = int(input())
    people = [-1]
    for i in range(1, n + 1):
        name, score, penalty = input().split()
        people.append((-int(score), int(penalty), name))
        sift_up(people, i)

    for i in range(n, 0, -1):
        print(people[1][2])
        if i > 1:
            people[1] = people.pop()
        sift_down(people, 1)


if __name__ == '__main__':
    main()
