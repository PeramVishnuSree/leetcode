# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.


class Solution:
    def canJump(self, nums):

        if len(nums) == 1:
            return True

        bol = False
        i = len(nums) - 1
        j = i - 1

        while i >= 0 and j >= 0:
            bol = False
            if nums[j] >= i - j:
                i = j
                j = j - 1
                bol = True
            else:
                j -= 1

        if i == 0 and bol is True:
            return True

        return False