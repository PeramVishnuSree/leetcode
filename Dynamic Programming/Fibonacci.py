# Recursive approach
# n refers to the nth fibonacci number in the sequence

class Fibonacci:
    memo = {1: 1, 2: 1}

    def fib_recursive(self, n):
        if n == 1 or n == 2:
            return 1
        return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)

    def fib_memoize(self, n):  # top-down memoization approach
        if n in self.memo:
            return self.memo[n]
        value = self.fib_memoize(n - 1) + self.fib_memoize(n - 2)
        self.memo[n] = value
        return value

    def bottom_up(self, n):  # bottom-down tabulation approach
        arr = [1, 1]
        if n == 1 or n == 2:
            return 1
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])

        return arr[n - 1]
