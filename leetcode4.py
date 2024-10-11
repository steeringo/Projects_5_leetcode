# 80. Remove Duplicates from Sorted Array II

class Solution(object):
    def removeDuplicates(self, nums):
        duplicates_count = {}
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in duplicates_count:
                duplicates_count[nums[i]]+=1
            else:
                duplicates_count[nums[i]] = 1

            if duplicates_count[nums[i]]>2:
                nums.pop(i)

        nums.sort()
        k = len(nums)

        return k, nums
    
nums = [1,1,1,2,2,3]
x = Solution().removeDuplicates(nums)
print(x)
