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