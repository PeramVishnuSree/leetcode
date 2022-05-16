# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.



def isValid(s):
    stack = []
    l1, l2 = ['[', '(', '{'], [']', ')', '}']
    for i in s:
        if i in l1:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if l1.index(stack.pop()) == l2.index(i):
                continue
            else:
                return False
    if len(stack) == 0:
        return True
    return False