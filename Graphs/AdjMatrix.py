class Vertex:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self.vertices = []
        self.d = {}
        self.indices = []

    def addvertex(self, v):
        if v in self.d:
            print('vertex already exists')
            return
        v = Vertex(v)
        self.vertices.append(v)
        self.d[v.value] = self.vertices.index(v)
        for lst in self.indices:
            lst.append(0)
        self.indices.append([0])
        for i in range(len(self.vertices)-1):
            self.indices[len(self.indices)-1].append(0)
        print(self.indices)

    def addedge(self, c1, c2):
        for key, value in self.d.items():
            if key == c1:
                v1 = value
            if key == c2:
                v2 = value

        self.indices[v1][v2] = 1
        self.indices[v2][v1] = 1

    def display(self):
        return self.indices