"""
Website: Leetcode
URL: https://leetcode.com/problems/non-decreasing-array/

Problem statement:
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
    Input: [4,2,3]
    Output: True
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
    Input: [4,2,1]
    Output: False
    Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000].

"""

from typing import List


class Solution:
    # def check_subarray(self, x:int, y:int, z:int) -> int:
    #     if x <= y and y <= z: # 2 3 4
    #         return 0
    #     if x <= y and y > z: # 3 4 2
    #         return 0
    #     if x > y: # 4 3 x
    #         if y > z: # 4 3 1
    #             return 2
    #         if y <= z: # 4 3 5
    #             return 0

    def check_possibility(self, nums: List[int]) -> bool:
        # nums = [nums[0]] + nums + [nums[-1]]
        print(nums) 
        def check_subarray(x: int, y: int, z: int) -> int:
            print(x, y, z) 

            if x <= y and y <= z:
                return 0
            if x <= y and y > z:
                if x == y:
                    return 0  # 3 3 2
                if x > z: # 2 6 1
                    return 2
                return 0
            if x > y:
                if y > z:
                    return 2
                if y <= z:
                    return 1



        prev_i = 0
        next_i = 2
        n = 0
        for num in nums[1:-1]:
            r = check_subarray(nums[prev_i], num, nums[next_i])
            print(r)
            if r == 2:
                return False
            n = n + r
            if n > 1:
                return False
            prev_i = prev_i + 1
            next_i = next_i + 1
        return True


if __name__ == "__main__":
    s = Solution()
    # assert s.check_possibility([3,2,3,2,4]) == False
    # assert s.check_possibility([4, 2, 3]) == True
    # assert s.check_possibility([4, 3, 2]) == False
    # assert s.check_possibility([3,4,2,3]) == False
    # assert s.check_possibility([-1, 4, 2, 3]) == True
    # assert s.check_possibility([1,5,4,6,7,10,8,9]) == False
    # assert s.check_possibility([2,3,3,2,4]) == True
    assert s.check_possibility([3,3,2,2]) == False
