# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match,
# such that there is a bijection between a letter in pattern and a non-empty word in s.


class Solution:
    def wordPattern(self, pattern, s) :
        l = s.split(' ')
        k = len(pattern)
        d = {}
        arr = []
        if k != len(l):
            print(k, len(l))
            return False

        for i in range(k):
            if pattern[i] in d:
                if d[pattern[i]] == l[i]:
                    continue
                else:
                    return False

            else:
                if l[i] in arr:
                    return False
                d[pattern[i]] = l[i]
                arr.append(l[i])

        return True