import sys
x = input()
temp = map(int, sys.stdin.readline().split())
tots = []
nums = []
for i in xrange(4007):
    tots.append(0)
nums = [0 for i in xrange(2001)]
for i in xrange(len(temp)):
    nums[temp[i]] += 1
    if nums[temp[i]]%2 == 0:
        tots[temp[i]*2]+= 1
for i in xrange(1, 2001):
    if nums[i]:
        for j in xrange(i+1, 2001):
            if nums[j]:
                tots[i+j] += min(nums[i], nums[j])
min1 = 1
count = 0
for i in xrange(len(tots)):
    if tots[i]>min1:
        min1 = tots[i]
        count = 0
    if tots[i] == min1:
        count+=1
print(min1),
print(count)
