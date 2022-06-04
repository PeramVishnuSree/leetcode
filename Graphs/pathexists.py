class Solution:
    def validPath(self, n, edges, source, destination):
        if n == 1:
            return True
        arr = []
        for i in edges:
            if i[0] == source and i[1] == destination:
                return True
        q = [source]
        while len(q) is not 0:
            for edge in edges:
                if q[0] == edge[0] and edge[1] not in arr:
                    q.append(edge[1])
                    arr.append(edge[1])
                if q[0] == edge[1] and edge[0] not in arr:
                    q.append(edge[0])
                    arr.append(edge[0])
            del q[0]

        if destination in arr:
            return True
        return False
