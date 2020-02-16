import sys

class Solution:
    def fibonacci(self, n: int) -> int:
        # memoization
        fib_array = [0, 1] + [-1]*(n-1)
        if fib_array[n] != -1:
            return fib_array[n]
        else:
            if fib_array[n-1] == -1:
                fib_array[n-1] = self.fibonacci(n-1)
            if fib_array[n-2] == -1:
                fib_array[n-2] = self.fibonacci(n-2)
        fib_array[n] = fib_array[n-1] + fib_array[n-2]
        return fib_array[n]


if __name__ == "__main__":
    s = Solution()
    assert s.fibonacci(0) == 0
    assert s.fibonacci(9) == 34
    assert s.fibonacci(26) == 121393
    print("finished without error")
