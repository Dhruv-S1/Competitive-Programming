import sys

# NOTE this solution yields 30/100 points

def main():
    n, q = map(int, raw_input().split())
    a = []
    temp = []
    temp = map(int, sys.stdin.readline().split())
    if q>15000:
        z = max(temp)
    else:
        z = 1000001
    for i in xrange(z):
        a.append(0)
    for i in xrange(len(temp)):
        min1 = temp[i]
        a[min1] += 1
        for j in xrange(i+1, len(temp)):
            if temp[j]<min1:
                min1 = temp[j]
            a[min1] += 1
    b = []
    current = 0
    for i in xrange(len(a)):
        current += a[i]
        b.append(current)
    a = []
    for i in range(q):
        num1, num2 = map(int, sys.stdin.readline().split())
        print((n+((n-1)*(n))/2) - (b[num1-1]+ (b[len(b)-1]-b[num2])))
main()
