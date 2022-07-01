# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.



class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        if node.neighbors is None:
            return Node(node.val)
        d = {}
        arr = []
        q = [node]
        while len(q) != 0:
            k = q[0]
            del q[0]
            arr.append(k)
            for neighbor in k.neighbors:
                if neighbor not in arr and neighbor not in q:
                    q.append(neighbor)

        for item in q:
            arr.append(q.pop())

        for i in arr:
            d[i.val] = []
            for j in i.neighbors:
                d[i.val].append(j.val)

        head = None
        qd = {}
        for key in d:
            qd[key] = Node(key)

        print(d)
        print(qd)

        for num, nums in d.items():
            if head is None:
                head = qd[num]
            cur = qd[num]
            for n in nums:
                cur.neighbors.append(qd[n])

        return head