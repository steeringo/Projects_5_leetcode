# 27. Remove Element

class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            for i in nums:
                if i == val:
                    nums.remove(i)
        k = len(nums)
        return k, nums

#   Better Optimization
class Solutionv2:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index, nums

nums = [0,1,2,2,3,0,4,2]
val = 2
x = Solution().removeElement(nums, val)
print(x)

y = Solution().removeElement(nums, val)
print(y)
