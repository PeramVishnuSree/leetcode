# given and integer, return true if it's a palindrome. false otherwise

class Solution:
    def isPalindrome(self, x):
        num = str(x)
        i = 0
        j = len(num) - 1
        while j > i:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1

        return True