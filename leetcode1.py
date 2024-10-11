import random

m = int(input("length of first numbers: "))
n = int(input("length of second numbers: "))

if 0 > m:
    m = input("length of first numbers: ")
elif n > 200:
    n = input("length of second numbers: ")
else:
    pass

if 1 <= m + n <= 200:
    pass
else:
    m = input("length of first numbers: ")
    n = input("length of second numbers: ")


nums1 = []
nums2 = []

for i in range(m):
    nums1.append(random.randrange(1,10))


for i in range(n):
    nums1.append(0)
    nums2.append(random.randrange(1,10))

print(nums1)
print(nums2)
nums1.extend(nums2)
nums1 = [x for x in nums1 if x != 0]
nums1.sort()
print(nums1)


