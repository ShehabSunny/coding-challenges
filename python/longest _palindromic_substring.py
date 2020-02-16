"""
Website: Leetcode
URL: https://leetcode.com/problems/longest-palindromic-substring/

Problem statement:
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

class Solution():
    def is_palindrome(self, s:str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

    def longest_palindrome(self, s: str) -> str:
        for i in s:
            print(i)

        return s


if __name__ == "__main__":
    test_inputs = [
        "abcs",
        # "abb",
        # "babad",
    ]

    s = Solution()
    # for i in test_inputs:
    #     r = s.longest_palindrome(i)
    #     assert r == "abcs"

    print(s.is_palindrome("abccbaaa"))

    print("finished with no errors")