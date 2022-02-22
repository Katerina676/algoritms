def sift_down(heap, idx):
    length_heap = len(heap) - 1
    left = 2 * idx
    right = 2 * idx + 1
    if left > length_heap:
        return idx
    if right <= length_heap and heap[left] < heap[right]:
        index_largest = right
    else:
        index_largest = left

    if heap[index_largest] > heap[idx]:
        heap[index_largest], heap[idx] = heap[idx], heap[index_largest]
        idx = sift_down(heap, index_largest)
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


print(test())
