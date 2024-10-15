# 55. Jump Game

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        last_index = len(nums)-1
        for i in range(len(nums) -2, -1, -1):
            if nums[i]+i >= last_index:
                last_index = i
        return True if last_index == 0 else False
            


nums = [2,3,1,1,4]
x = Solution().canJump(nums)
print(x)