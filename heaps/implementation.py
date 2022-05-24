class MinBinaryHeap:
    def __init__(self):
        self._heap = []

    def __str__(self):
        return f'{self._heap}'

    __repr__ = __str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        return self._heap[0]

    def _parent(self, index):
        if index == 1:
            return
        ans = self._heap[(index // 2) - 1]
        return ans

    def _leftChild(self, index):
        try:
            return self._heap[2 * (index - 1) + 1]
        except:
            return

    def _rightChild(self, index):
        try:
            return self._heap[2 * (index - 1) + 2]
        except:
            return

    def insert(self, item):
        if len(self._heap) == 0:
            self._heap.append(item)
        else:
            self._heap.append(item)
            k = len(self._heap)
            while item < self._parent(k):
                m = k - 1
                n = (k // 2) - 1
                k = n + 1
                self._heap[m], self._heap[n] = self._heap[n], self._heap[m]
                if k - 1 == 0:
                    break

    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self) == 0:
            return None
        elif len(self) == 1:
            deleted = self._heap[0]
            self._heap = []
            return deleted
        else:
            deleted = self._heap[0]
            self._heap[0] = self._heap[(len(self._heap) - 1)]
            del self._heap[(len(self._heap) - 1)]
            item = self._heap[0]
            k = 1
            try:
                while item > self._rightChild(k) or item > self._leftChild(k):
                    if self._rightChild(k) == self._leftChild(k):
                        self._heap[2 * (k - 1) + 1], self._heap[k - 1] = self._heap[k - 1], self._heap[2 * (k - 1) + 1]
                        k = 2 * k

                    elif self._rightChild(k) < self._leftChild(k):
                        self._heap[2 * (k - 1) + 2], self._heap[k - 1] = self._heap[k - 1], self._heap[2 * (k - 1) + 2]
                        k = 2 * k + 1

                    else:
                        self._heap[2 * (k - 1) + 1], self._heap[k - 1] = self._heap[k - 1], self._heap[2 * (k - 1) + 1]
                        k = 2 * k
            except:
                return deleted
            return deleted


def heapSort(numList):

    lst = []
    b = len(numList)
    min_heap = MinBinaryHeap()
    for i in numList:
        min_heap.insert(i)
    while min_heap.deleteMin() is not None:
        lst.append(min_heap.deleteMin())
    return lst
