# 189. Rotate Array
class Solution(object):
    def rotate(self, nums, k):

        # % - modulo (reszta)
        k = k % len(nums)

        # Slicing array
        nums[:] = nums[-k:] + nums[:-k]
        return nums


nums = [1,2,3,4,5,6,7]
k = 3
x = Solution().rotate(nums, k)
print(x)