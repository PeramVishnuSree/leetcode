#Given two integers left and right, return the count of numbers in the inclusive range [left, right]
# having a prime number of set bits in their binary representation.

def countPrimeSetBits(left, right):
    ans = 0
    for i in range(left, right + 1):
        bit = str(bin(i))[2:]
        count = 0
        for k in bit:
            if k == "1":
                count += 1
        if count in [2, 3, 5, 7, 11, 13, 17, 19]:
            ans += 1

    return ans

