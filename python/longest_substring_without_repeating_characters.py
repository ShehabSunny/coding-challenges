"""
Website: Leetcode
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/


Problem statement:
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        seen_chars = {}
        start_from = 0
        end_to = 0
        l = 0
        for i, x in enumerate(s):
            
            if x in seen_chars:
                start_from = max(seen_chars[x] + 1, start_from)
            end_to = i 
            seen_chars[x] = i
            l = max(l, (end_to - start_from))
        return l + 1


if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLongestSubstring("")
    print(res)