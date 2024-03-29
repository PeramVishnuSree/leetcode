# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x):
        # -2147483648 to 2147483647
        sign = True
        if x < 0:
            sign = False
            x = -1 * x

        rev = ''
        x = str(x)
        for i in range(1, len(x) + 1):
            rev += x[-1 * i]

        if sign is False:
            rev = -1 * int(rev)
        else:
            rev = int(rev)

        if rev > 2147483647 or rev < -2147483647 : return 0
        return rev
