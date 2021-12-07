# given a string, find the length of the longest substring.
# Note that it's not the longest sub sequence.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxl = 0
        lst = []
        for i in s:
            lst.append(str(ord(i)))
        s = lst
        for i in range(len(s)):
            ls = []
            for j in range(i, len(s)):
                if s[j] in ls:
                    if len(ls) > maxl:
                        maxl = len(ls)
                    break

                else:
                    print('here')
                    ls.append(s[j])
                    if j == len(s) - 1 and len(ls) > maxl:
                        maxl = len(ls)

        return maxl