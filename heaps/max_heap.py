# implement max heap class with __init__ and insert method\\

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Max_Heap:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self. root is None:
            self.root = Node(value)
            return
