# In English, we have a concept called root, which can be followed by some other word to form another longer word
# - let's call this word successor. For example, when the root "an" is followed by the successor word "other",
# we can form a new word "another".

# Given dictionary (a list) consisting of many roots and a sentence consisting of words separated by spaces,
# replace all the successors in the sentence with the root forming it.
# If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.


class Solution:
    def replaceWords(self, dictionary, sentence) :
        t = Trie()
        for word in dictionary:
            t.insert(word)
        s = sentence.split(' ')
        for i in range(len(s)):
            ans = t.lookup(s[i])
            if ans is False:
                continue
            s[i] = ans

        ans = ' '.join(s)
        return ans


class node:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.head = node()

    def insert(self, word):
        cur = self.head
        for char in word:
            if char not in cur.children:
                cur.children[char] = node()

            cur = cur.children[char]
        cur.children['*'] = None

    def lookup(self, word):
        cur = self.head
        s = ''
        for char in word:
            if "*" in cur.children:
                return s
            if char in cur.children:
                s += char
            else:
                return False

            cur = cur.children[char]

        return s