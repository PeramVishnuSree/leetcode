# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
#
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


class Solution:
    def findJudge(self, n, trust):
        g = Graph()
        for i in range(1, n + 1):
            g.addvertex(i)
        for k in trust:
            g.additem(k[0], k[1])
        d = g.getgraph()

        ans = -1
        for key, value in d.items():
            if value == []:
                arr = False
                for m, n in d.items():
                    if m == key:
                        continue
                    if key not in n:
                        arr = True
                if arr == False:
                    ans = key
        return ans


class Graph:

    def __init__(self):
        self.log = {}

    def addvertex(self, vertex):
        if vertex in self.log:
            return
        self.log[vertex] = []

    def additem(self, vertex, n):
        self.log[vertex].append(n)

    def getgraph(self):
        return self.log