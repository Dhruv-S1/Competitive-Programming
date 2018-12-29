import sys

#NOTE: This partial solution gives 90/100 points

def main():
    n, m = map(int, raw_input().split())
    good = []
    bad = []
    for i in xrange(n):
        num1, num2 = map(int, sys.stdin.readline().split())
        if num2 == 1:
            bad.append(num1)
        else:
            good.append(num1)
    good.sort()
    bad.sort()
    for i in xrange(1, len(bad)):
        bad[i] += bad[i-1]
    for i in xrange(1, len(good)):
        good[i] += good[i-1]
    total = 0 
    best = 0
    for i in xrange(len(good)):
        current = good[i]
        if current>m:
            break
        if (i+1)*2>total:
            total = (i+1)*2
        if current == m:
            if (i+1)*2>total:
                total = (i+1)*2
        else:
            start = 0
            end = len(bad)-1
            mid = 0
            while True:
                mid = (start+end)/2
                if end == start:
                    if bad[end]<=m-good[i]:
                        if (end+1)+(i+1)*2>total:
                            total = (end+1)+(i+1)*2
                        break
                    if bad[start]<=m-good[i]:
                        if (start+1)+(i+1)*2>total:
                            total = (start+1)+(i+1)*2
                        break
                    break
                if end-start == 1:
                    if bad[end]<=m-good[i]:
                        if (end+1)+(i+1)*2>total:
                            total = (end+1)+(i+1)*2
                        break
                    if bad[start]<=m-good[i]:
                        if (start+1)+(i+1)*2>total:
                            total = (start+1)+(i+1)*2
                        break
                    break
                if bad[mid] == m-good[i]:
                    if mid+1+(i+1)*2>total:
                        total = mid+1+(i+1)*2
                    break
                if bad[mid]>m-good[i]:
                    end = mid
                    continue
                if bad[mid]<m-good[i]:
                    start = mid
    for i in xrange(len(bad)):
        if bad[i]<m:
            if i>total:
                total = i

    print total
main()
