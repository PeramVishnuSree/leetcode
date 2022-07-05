# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
# and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
# connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


class Solution:
    def findCircleNum(self, isConnected):
        # DFS approach

        # convert to adjacency list
        adj = {}
        for i in range(len(isConnected)):
            adj[i + 1] = []
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    adj[i + 1].append(j + 1)

        print(adj)

        # DFS
        q, visited, provs = [], [], []
        for key, val in adj.items():
            if key not in visited:
                provs.append([key])

            if len(val) > 0:
                for conn in val:
                    if conn not in visited:
                        q.append(conn)
                        provs[len(provs) - 1].append(conn)
                        visited.append(conn)
            while len(q) > 0:
                for i in adj[q.pop()]:
                    if i not in visited:
                        visited.append(i)
                        provs[len(provs) - 1].append(i)
                        q.append(i)
            if len(visited) == len(adj):
                break

        return len(provs)