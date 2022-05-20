# given a text file, insert all the words in the file into a bst.
# write a function to return the anagrams of a word form the created bst.
# return "no match" the word doesn't correspond to the bst.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return ("Node({})".format(self.value))

    __repr__ = __str__


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, value):
        if self.root is None:
            _value = ''.join(sorted(value))
            value = {_value: [value]}
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):

        _value = ''.join(sorted(value))
        for x, y in node.value.items():
            key = x
        # equal to the value of the node condition
        if _value == key:
            node.value[_value].append(value)

        # greater than the value of the node (moves to the right side)
        elif _value > key:
            if node.right is None:
                node.right = Node({_value: [value]})
            else:
                self._insert(node.right, value)

        # less than the value of the node (moves to the left side)
        elif _value < key:
            if node.left is None:
                node.left = Node({_value: [value]})
            else:
                self._insert(node.left, value)

    def isEmpty(self):
        return self.root == None

    @property
    def printInorder(self):
        if self.isEmpty():
            return None
        else:
            self._inorderHelper(self.root)

    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left)
            print(node.value, end=' : ')
            self._inorderHelper(node.right)


class Anagrams:

    def __init__(self, word_size):
        self.word_size = word_size
        self._bst = BinarySearchTree()

    def create(self, file_name):
        with open(file_name) as f:
            contents = f.readlines()

        for line in contents:
            words = line.strip().split(' ')
            for word in words:
                if len(word) > self.word_size or len(word) == 0:
                    continue
                self._bst.insert(word)

    def getAnagrams(self, word):
        node = self._bst.root
        _value = ''.join(sorted(word))
        if _value in node.value:
            return node.value[_value]
        else:
            return self._getAnagrams(node, _value)

    def _getAnagrams(self, node, sorted_word):
        for x, y in node.value.items():
            key = x

        if sorted_word > key:
            if node.right is not None:
                return self._getAnagrams(node.right, sorted_word)
            else:
                return "No match"

        elif sorted_word < key:
            if node.left is not None:
                return self._getAnagrams(node.left, sorted_word)
            else:
                return "No match"

        else:
            return node.value[sorted_word]