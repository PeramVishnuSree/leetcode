# Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.
# Implement the ProductOfNumbers class:ProductOfNumbers() Initializes the object with an empty stream.
# void add(int num) Appends the integer num to the stream.
# int getProduct(int k) Returns the product of the last k numbers in the current list.
# You can assume that always the current list has at least k numbers.he test cases are generated so that, at any time,
# the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.


class ProductOfNumbers:

    def __init__(self):
        self.queue = []
        self.length = 0

    def add(self, num: int):
        self.queue.append(num)
        self.length +=1

    def getProduct(self, k: int):
        product = 1
        arr = self.queue[self.length-k:]
        if k == 0 or 0 in arr:
            return 0
        for i in arr:
            product *= i
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)