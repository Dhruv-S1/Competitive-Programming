from math import sqrt
import sys
def main():
    x = input()
    if x == 1:
        print 0
        sys.exit()
        
    cost = 0
    while True:
        hold = 0
        n = int(sqrt(x))+1
        prevx = 0
        prevx = x
        for i in xrange(2, n):
            if x%i == 0:
                hold = x/i
                x = x-hold
                break
    
        if x == prevx:
            x = x-1
            cost = cost+x
            if x == 1:
                print cost
                break
            continue
        else:
            cost += x/hold
main()
