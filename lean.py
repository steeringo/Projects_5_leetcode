import random

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        print(nums1)
        print(nums2)
        nums1.extend(nums2)
        nums1 = [x for x in nums1 if x != 0]
        nums1.sort()
        print(nums1)

m = int(input("length of first numbers: "))
n = int(input("length of second numbers: "))

if 0 > m:
    m = int(input("length of first numbers: "))
elif n > 200:
    n = int(input("length of second numbers: "))
else:
    pass

if 1 <= (m + n) <= 200:
    pass
else:
    m = int(input("length of first numbers: "))
    n = int(input("length of second numbers: "))

nums1 = []
nums2 = []

for i in range(m):
    nums1.append(random.randrange(1,10))


for i in range(n):
    nums1.append(0)
    nums2.append(random.randrange(1,10))

solution = Solution()
solution.merge(nums1, m, nums2, n)