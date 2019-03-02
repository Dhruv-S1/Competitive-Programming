import sys
from math import sqrt
from math import ceil

//NOTE this solution yields 5/100 points 

def main():
    n, q = map(int, raw_input().split())
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

    def update(a, squarearray, switch, val):
        blocknum = int(ceil(float(switch)/float(blocksize)))-1
        if a[switch-1] <0:
            squarearray[blocknum]+= (-1*a[switch-1])
        else:
            squarearray[blocknum]-=a[switch-1]
        squarearray[blocknum]+=val
        a[switch-1] = val
    a = []
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
        temp = map(str, sys.stdin.readline().split())
        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        if temp[0] == "Q":
            print query(a, squarearray, temp[1]-1, temp[2]-1)
        if temp[0] == "S":
            update(a, squarearray, temp[1], temp[2])
main()
