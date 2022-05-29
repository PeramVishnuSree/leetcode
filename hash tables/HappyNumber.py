# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# 1.  Starting with any positive integer, replace the number by the sum of the squares of its digits.
# 2. Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# 3. Those numbers for which this process ends in 1 are happy.
# 4. Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n):
        k = n
        arr = []
        while k != 1 and k not in arr:
            c = 0
            arr.append(k)
            k = str(k)
            for i in k:
                c += (int(i)) ** 2
            k = c

        if k in arr:
            return False
        return True