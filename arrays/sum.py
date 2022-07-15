# given an array of distinct integers and a target, return an array of
# arrays of integers that add up to the sum


class Solution:

    def combinationSum(self, candidates, target):

        sol = []
        l = len(candidates)
        candidates.sort()
        print(candidates)
        for i in range(l):
            sum = candidates[i]
            if sum > target:
                break
            arr = [sum]
            if sum == target:
                sol.append(arr)
            for j in range(i + 1, l):
                k = candidates[j] + sum
                print(k)
                if k > target:
                    break
                elif k < target:
                    arr.append(k - sum)
                    sum = k
                    if j == l - 1:
                        return sol
                    continue
                elif k == target:
                    arr.append(k - sum)
                    sol.append(arr)
                    break

        return sol