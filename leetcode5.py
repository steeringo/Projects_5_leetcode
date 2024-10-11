# 169. Majority Element
class Solution(object):
    def majorityElement(self, nums):
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        print(counter)
        for num in counter:
            if counter[num] > len(nums) // 2:
                return num

        return None
    
class Solutionv2(object):
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]
    
nums = [2,2,1,1,1,2,2]
x = Solutionv2().majorityElement(nums)
print(x)