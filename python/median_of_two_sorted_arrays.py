class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1 + nums2
        print(nums)


if __name__ == "__main__":
    s = Solution()
    s.findMedianSortedArrays(
        [1,3],
        [2]
    )