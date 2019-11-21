"""
Website: Leetcode
URL: https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

import math

class Solution():
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False
        x_str = str(x)
        for i in range(math.ceil(math.log(x, 10)/2)):
            if x_str[i] != x_str[(-i-1)]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(1221))
    print(s.isPalindrome(12321))
    print(s.isPalindrome(1))