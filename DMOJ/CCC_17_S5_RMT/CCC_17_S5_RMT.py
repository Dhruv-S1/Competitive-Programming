import sys
from math import sqrt
from math import ceil

#NOTE this partial solution yields 5/15 points

def main():
    n, m, q = map(int, raw_input().split())
    global blocksize
    blocksize = int(sqrt(n))
    def query(a, squarearray, left, right):
        tot = 0
        while left<right and left%blocksize!=0:
            tot+=a[left]
            left+=1
        while left+blocksize<=right:
            tot+= squarearray[left/blocksize]
            left+=blocksize
        while left<=right:
            tot+= a[left]
            left+=1
        return tot
    def update(a, squarearray, train):
        hold = 0
        hold = a[d[train][len(d[train])-1]-1]
        blocknum = 0
        for i in range(len(d[train])-1, 0, -1):
            blocknum = int(ceil(float(d[train][i])/float(blocksize)))-1
            squarearray[blocknum]-= a[d[train][i]-1]
            squarearray[blocknum] += a[d[train][i-1]-1]
            a[d[train][i]-1] = a[d[train][i-1]-1]
        blocknum = int(ceil((float(d[train][0])/float(blocksize)))-1)
        squarearray[blocknum]-=a[d[train][0]-1]
        squarearray[blocknum]+=hold
        a[d[train][0]-1] = hold
        
    
    temp = []
    temp  = map(int, sys.stdin.readline().split())
    d = {}
    for i in xrange(1, m+1):
        d[i] = []
    for i in xrange(len(temp)):
        d[temp[i]].append(i+1)
    temp = []
    a = map(int, sys.stdin.readline().split())
    squarearray = []
    hold = 0
    count = 0
    
    for i in xrange(len(a)):
        if i%blocksize == 0 and i != 0:
            squarearray.append(hold)
            hold = 0
    
        hold += a[i]
    if hold !=0:
        squarearray.append(hold)
    
    for i in xrange(q):
        temp = []
        temp = map(int, sys.stdin.readline().split())
        if len(temp) == 3:
            print query(a, squarearray, temp[1]-1, temp[2]-1)
        if len(temp) == 2:
            update(a, squarearray, temp[1])
main()
