# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.


class Solution:
    def removeKdigits(self, num, k):

        if k >= len(num):
            return "0"

        stack = []
        for val in num:
            while stack and k and int(stack[-1]) > int(val):
                stack.pop()
                k -= 1
            stack.append(val)
        print(stack, k)

        while k > 0:
            stack.pop()
            k -= 1

        return str(int("".join(stack)))
