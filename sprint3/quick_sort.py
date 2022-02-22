# --- ПРИНЦИП РАБОТЫ ---
# Реализация быстрой сортировки с двумя указателями границ, которые сравнивают больше или меньше опорного элемента
# и меняются местами в зависимости от этого, пока они не сойдутся.
# --- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ ---
# Базовый случай рекурсии когда элемент равен одному. Остановка указателей происходит когда они встречаются
# это гарантирует что они отсортировали свои половины. Тк не выделяется дополнительная память на список сортированных
# элементов происходит сортировка in-place, когда элементы меняются местами в самом массиве.
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
# Алгоритм быстрой сортировки работает в лучше и среднем случае за O(nlog n), а в худшем случае O(n^2), но это исключено
# т.к мы выбираем элемент из середины массива.
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
# Память тратится на рекурсию , которая хранит элементы в стеке вызовов глубиной O(log n) в среднем и лучшем случае
# и O(n) в худшем случае.
# id 64210126
def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left, right


def quick_sort(arr, left, right):
    if left >= right:
        return arr
    left_part, right_part = partition(arr, left, right)
    quick_sort(arr, left, right_part)
    quick_sort(arr, left_part, right)
    return arr


def main():
    n = int(input())
    people = []
    for _ in range(n):
        name, score, penalty = input().split()
        people.append((-int(score), int(penalty), name))
    quick_sort(people, 0, len(people)-1)
    for i in people:
        print(i[2])


if __name__ == '__main__':
    main()
