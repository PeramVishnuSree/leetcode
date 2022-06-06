# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def two_number (nums,target):

    # If a number is exactly half of the target a repeats only once, the program may return the same index twice.
    # This part of the code eliminates that problem
    for i in nums:
        if i == target / 2 and nums.count(i) == 1:
            continue

        # if the same number that repeats itself twice adds up to the target
        if target - i in nums:
            a = nums.index(i)
            if nums.count(target - i) == 1:
                b = nums.index(target - i)
                return a, b

            # if it's two different numbers in the list that add up to the target
            elif nums.count(target - i) > 1:
                k = len(nums[:nums.index(i) + 1])
                nums = nums[nums.index(i) + 1:]
                for m in nums:
                    if m == i:
                        b = k + nums.index(m)
                        return a,b