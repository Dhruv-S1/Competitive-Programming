import math
import sys
def isprime(n):
    count = 0
    for i in xrange(1, int(math.ceil(math.sqrt(n)))+1):
        if count>1:
            return False
        if n%i == 0:
            count = count + 1
    if count == 1 and n != 1:
        return True
    else:
        return False

def binary(start, end, num):
    while True:
        mid = (start+end)/2
        if end-start == 1:
            if b[end] <num:
                return end
            else:
                return start
        
        if b[mid]>num:
            end = mid
        if b[mid] <num:
            start = mid
        if b[mid] == num:
            return mid-1

b = []
b.append(2)
for i in xrange(3, 100000, 2):
    if isprime(i):
        b.append(i)
x = input()
temp = []
temp = map(int, raw_input().split())
for i in range(len(temp)):
    if temp[i] == 1 or temp[i] == 2:
        print("no can do")
    else:
        print(b[binary(0, len(b), temp[i])])
