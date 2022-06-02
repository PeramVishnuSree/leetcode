class Solution:
    def lexicalOrder(self, n):
        s = []
        for i in range(1, n + 1):
            s.append(str(i))
        s.sort()
        return s