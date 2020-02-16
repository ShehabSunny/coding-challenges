"""
Website: Leetcode
URL: https://leetcode.com/problems/buddy-strings/

Problem statement:
Given two strings A and B of lowercase letters, 
return true if and only if we can swap two letters in A so that the result equals B.


Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""

class Solution:
    def __init__(self):
        pass

    def buddy_string(self, A: str, B: str) -> bool:
        if len(A) > 20000 or len(B) > 20000:
            return False 

        if len(A) != len(B):
            return False
        seen = []
        if A == B:
            for i, j in zip(A, B):
                if i in seen:
                    return True
                else:
                    seen.append(i)
        else:
            pairs = []
            for i, j in zip(A, B):
                if i != j:
                    pairs.append((i, j))

            return len(pairs) == 2 and (pairs[0][0] == pairs[1][1] and  pairs[0][1] == pairs[1][0])
    

if __name__ == "__main__":
    a = "abc" # aabc aacb
    b = "acb"
    s = Solution()
    r = s.buddy_string(a, b)
    print(r)