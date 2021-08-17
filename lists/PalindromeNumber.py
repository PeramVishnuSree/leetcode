# Given an integer x, return true if x is palindrome integer.
def isPalindrome(self, x: int) -> bool:
    if x * -1 > 0:
        return "false"
    x = str(x)
    s = ""
    for i in range(1, len(x) + 1):
        s = s + x[len(x) - i]

    if x == s:
        return "true"
    else:
        return "false"