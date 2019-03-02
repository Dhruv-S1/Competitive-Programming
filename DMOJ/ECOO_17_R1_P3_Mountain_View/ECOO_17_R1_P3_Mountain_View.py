import sys

for i in xrange(10):
    x = input()
    temp = map(int, sys.stdin.readline().split())
    min1 = -1
    cursmal = 0
    for j in xrange(len(temp)):
        count = 0
        curbig = 0
        marker = 0
        for k in xrange(j-1, -1, -1):
            if temp[k] >=curbig or k == j-1:
                curbig = temp[k]
                count+=1
                if curbig>temp[j]:
                    break
            else:
                continue
            
        curbig = 0
        for k in xrange(j+1, len(temp)):
            if temp[k] >=curbig or k == j+1:
                curbig = temp[k]
                count+=1
                if curbig>temp[j]:
                    break
            else:
                continue
        if count >min1:
            min1 = count
            cursmal = j+1
    print cursmal
