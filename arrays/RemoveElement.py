#Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.

def removeElement(nums, val) :
    x = nums.count(val)
    for i in range(x):
        nums.remove(val)

    return(nums)