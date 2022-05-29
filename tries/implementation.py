# implement class Try using dictionaries

class Trie:
    def __init__(self):
        self.head = {'*': '*'}

    def insert(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}

            cur = cur[ch]

        cur['*'] = '*'

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        return False