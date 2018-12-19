import sys

def getsum(BITTree,i):
    s = 0
    i = i+1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s



def updatebit(BITTree , n , i ,v):
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)

def main():
    y = input()
    BITTree = []
    for i in xrange(y+1):
        BITTree.append(0)
    temp = map(int, sys.stdin.readline().split())
    temp1 = []
    
    for i in xrange(len(temp)):
        temp1.append(tuple((temp[i], 999999, i)))
    
    x = input()
    for i in xrange(x):
        num1, num2, num3 = map(int, sys.stdin.readline().split())
        temp1.append((num3, num1, num2, i))
    q = [0]*(x+1)
    temp1.sort()
    temp1.reverse()
    count = 0
    
    for i in xrange(len(temp1)):
        if len(temp1[i]) == 3:
            j = temp1[i][2]
            updatebit(BITTree, len(BITTree)-1, j, temp1[i][0])
            count+=1
        else:
            if temp1[i][1] == temp1[i][2]:
                if temp[temp1[i][1]]>=temp1[i][0]:
                    q[temp1[i][3]] = temp[temp1[i][1]]
                else:
                    q[temp1[i][3]] = 0
                continue
            q[temp1[i][3]] = getsum(BITTree, temp1[i][2]) - getsum(BITTree, temp1[i][1]-1)
    for i in xrange(len(q)-1):
        print(q[i])
main()
