# 26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        duplicates = []
        # Iterate over the list in reverse order
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in duplicates:
                nums.pop(i)
            else:
                duplicates.append(nums[i])
        
        k= len(nums)
        return k, nums

class Solutionv2(object):
    def removeDuplicates(self, nums):
        # index to replace duplicates
        index = 1
        # Start from the second element and iterate
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1

        # Return the modified length
        return index, nums[:index]

nums = [0,0,1,1,1,2,2,3,3,4]
x = Solution().removeDuplicates(nums)
print(x)

y = Solutionv2().removeDuplicates(nums)
print(y)