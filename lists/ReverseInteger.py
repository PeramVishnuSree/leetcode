#Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.


def reverse(x):
    x = str(x)
    sol = ""
    if x[0] == '-':
        sol = "-"
        x = x[1:]
    if x[len(x) - 1] == 0:
        x = x[:len(x) - 1]
    for i in range(1, len(x) + 1):
        sol = sol + x[-1 * i]
    sol = int(sol)

    if sol <= 2147483648 and sol >= -2147483648:
        return sol
    else:
        return 0

print (reverse(345))


