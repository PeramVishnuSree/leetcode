# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:

    def search(self, nums, target):
        # binary search

        index = 0

        while len(nums) > 0:
            m = len(nums) // 2
            k = nums[m]

            if k == target:
                return index + m
            elif k > target:
                nums = nums[:m]
            else:
                nums = nums[m + 1:]
                index += m + 1

        return -1