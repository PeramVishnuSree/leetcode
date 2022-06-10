# Design your implementation of the circular queue. The circular queue is a linear data structure in which
# the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to
# the first position to make a circle. It is also called "Ring Buffer".
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
# In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front
# of the queue. But using the circular queue, we can use the space to store new values.


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.length = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.length:
            self.queue.append(value)
            return True

    def deQueue(self) -> bool:
        if len(self.queue) > 0:
            del self.queue[0]
            return True

    def Front(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[len(self.queue)-1]

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.queue) == self.length:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()