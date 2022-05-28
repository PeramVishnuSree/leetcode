# given a string, return the length of the longest sub string

class Solution:
    def lengthOfLongestSubstring(self, s):
        p1 = 0
        highest = 1
        if len(s) == 0:
            return 0
        for i in range(1, len(s)):
            while s[i] in s[p1:i]:
                p1 += 1
            l = len(s[p1:i + 1])
            if l > highest:
                highest = l

        return highest