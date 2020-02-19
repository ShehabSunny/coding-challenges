"""
Website: leetcode
URL: https://leetcode.com/problems/longest-common-prefix/


Problem statement:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


from typing import List


class Solution:
    def __init__(self):
        super().__init__()

    def longest_common_prefix(self, strs: List[str]) -> str:
        lcp = ""
        if len(strs) == 0:
            return lcp
        c = 0
        for idx, c in enumerate(strs[0]):
            for p in strs[1:]:
                if len(p) <= idx:
                    return lcp

                if c != p[idx]:
                    return lcp
            lcp = lcp+c
        return lcp


if __name__ == "__main__":
    s = Solution()
    inp = ["flower","flow","flight"]
    out = s.longest_common_prefix(inp)
    print(out)
    print(out == "fl")


"""
Time complexity: O(S) where S is the sum of all strings in the array
Space complexity: O(N)
"""