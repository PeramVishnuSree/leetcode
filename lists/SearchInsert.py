# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        for i in nums:
            if i < target and nums.index(i) == len(nums) - 1:
                return nums.index(i) + 1
            elif i > target:
                return nums.index(i)