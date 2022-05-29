# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        ln = len(nums) / 2
        for key, val in d.items():
            if val > ln:
                return key