# Design a class to find the kth largest element in a stream.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

class KthLargest:

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        l = len(self.nums)
        return self.nums[l-self.k]

