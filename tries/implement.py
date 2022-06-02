class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        cur = self.head
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]

        cur.end = True
        print('done')

    def search(self, word):
        cur = self.head
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        if cur.end is False:
            return 'prefix'

        return True