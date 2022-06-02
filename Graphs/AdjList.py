class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.neighbors = []

class Graph:
    def __init__(self):
        self.adjlist = []

    def additem(self, vertex, adj=list()):

        v = Vertex(vertex)
        v.neighbors = adj
        self.adjlist.append(v)
        return

    def display(self):
        d = {}
        for i in self.adjlist:
            d[i.vertex] = i.neighbors
        return d

    def deletevertex(self, v):

        for k in self.adjlist:
            if k.vertex == v:
                self.adjlist.remove(k)

        for i in range(len(self.adjlist)):
            if v in self.adjlist[i].neighbors:
                self.adjlist[i].neighbors.remove(v)

        return