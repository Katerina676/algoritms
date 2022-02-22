def sift_up(heap, idx):
    if idx == 1:
        return idx
    parent = idx // 2
    if heap[parent] > heap[idx]:
        return idx
    else:
        heap[parent], heap[idx] = heap[idx], heap[parent]
        return sift_up(heap, parent)


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


print(test())
