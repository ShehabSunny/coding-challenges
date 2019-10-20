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
    def longest_palindrome(self, s: str) -> str:
        return s


if __name__ == "__main__":
    test_inputs = [
        "abcs",
        "abb",
        "babad",
    ]

    s = Solution()
    for i in test_inputs:
        print(s.longest_palindrome(i))
