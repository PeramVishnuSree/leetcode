# Given a list of numbers, find the kth largest number.

class Solution:
    def findKthLargest(self, nums, k) :
        nums.sort()
        return nums[len(nums)-k]