# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as a 2D integer array edges, where
# each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
# Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
#
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
#
# Given edges and the integers n, source, and destination, return true if
# there is a valid path from source to destination, or false otherwise.



class Solution:
    def validPath(self, n, edges, source, destination):
        if n == 1:
            return True
        g = Graph()
        for i in edges:
            g.add_connection(i[0], i[1])
        arr = g.bfs(source)
        for ar in arr:
            for ele in ar:
                if ele == destination:
                    return True

        return False


class Queue:
    def __init__(self):
        self.q = []

    def isempty(self):
        if len(self.q) > 0:
            return False
        return True

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if self.isempty() is True:
            return
        k = self.q[0]
        del self.q[0]
        return k


class Vertex:
    def __init__(self, name):
        self.vertex = name
        self.neighbors = []


class Graph:
    def __init__(self):
        self.graph = []

    def add_vertex(self, v):
        v = Vertex(v)
        self.graph.append(v)

    # For directed graphs
    def add_neighbor(self, v, n):
        for i in self.graph:
            if i.vertex == v:
                i.neighbors.append(n)
                return

        v = Vertex(v)
        v.neighbors.append(n)
        self.graph.append(v)

    # For undirected graphs
    def add_connection(self, m, n):
        a = True
        b = True
        for i in self.graph:
            if i.vertex == m:
                i.neighbors.append(n)
                a = False
            if i.vertex == n:
                i.neighbors.append(m)
                b = False

        if a is True:
            k = Vertex(m)
            k.neighbors.append(n)
            self.graph.append(k)

        if b is True:
            l = Vertex(n)
            l.neighbors.append(m)
            self.graph.append(l)

    def getgraph(self):
        d = {}
        for i in self.graph:
            d[i.vertex] = i.neighbors
        return d

    def bfs(self, start):
        arr = []
        q = Queue()
        visited = []
        d = self.getgraph()
        q.enqueue(start)
        while q.isempty() is False:
            print('eer')
            m = q.dequeue()
            visited.append(m)
            ar = []
            for i in d[m]:
                if i not in visited:
                    q.enqueue(i)
                    ar.append(i)
            if len(ar) > 0:
                arr.append(ar)

        return arr