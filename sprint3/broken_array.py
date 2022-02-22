# --- ПРИНЦИП РАБОТЫ ---
# Реализация бинарного поиска в половинках отсортированного массива.Для этого мы срвниваем всегда левую и правую границу
# с центром, и сраниваем с искомым элементом, чтобы понять в какой части половинки продолжать поиск.
# --- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ ---
# Мы сравниваем края массива и его середину с искомым элементом и таким образом понимаем в какой половине искать дальше
# такая операция сокращает поиск в два раза.Если элемент не будет найден или границы сомкнутся мы вернем -1.
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
# Сложность алгоритма как у бинарного поиска O(log n), потому что наш поиск сокращается в два раза.
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
# Бинарный поиск без использования рекурсии хранит определенное количество данных и потребляет O(1) памяти.
# id 64243186
def broken_search(nums, target):
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 21) == 1
    result = broken_search([19, 21, 100, 101, 1, 4, 5, 7, 12], 5)
    assert result == 6, f'Wrong answer: {result}'
    result = broken_search([1, 2, 3, 4, 5, 6, 7, 8, 0], 7)
    assert result == 6, f'Wrong answer: {result}'
    result = broken_search([100, 0, 1, 2, 3, 44, 55, 73, 99], 0)
    assert result == 1, f'Wrong answer: {result}'
    result = broken_search([100, 0, 1, 2, 3, 44, 55, 73, 99], 99)
    assert result == 8, f'Wrong answer: {result}'
    result = broken_search([100, 0, 1, 2, 3, 44, 55, 73, 99], 100)
    assert result == 0, f'Wrong answer: {result}'
    result = broken_search([100, 0, 1, 2, 3, 44, 55, 73, 99], 101)
    assert result == -1, f'Wrong answer: {result}'
    result = broken_search([5, 6, 7, 8, 9, 0, 1, 2, 3, 4], 0)
    assert result == 5, f'Wrong answer: {result}'
    result = broken_search([1], 1)
    assert result == 0, f'Wrong answer: {result}'
    arr = [5, 1]
    assert broken_search(arr, 1) == 1
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test()
