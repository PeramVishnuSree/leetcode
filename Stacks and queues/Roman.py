# Given a roman number as a string,
# return an integer corresponding to the string

class Solution:
    def romanToInt(self, s):
        priority = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        stack = list(s)
        stack.reverse()
        k = 0
        p = priority[stack[0]]
        for i in stack:
            if priority[i] >= p:
                k += priority[i]
            else:
                k -= priority[i]
            p = priority[i]
        return k