from math import sqrt
def main():
    a = []
    for i in xrange(1000001):
        a.append(False)
    j = 2
    while j*j<=1000000:
        if not a[j]:
            for i in range(j*2, 1000001, j):
                a[i] = True
        j+=1
    a[0] = True
    a[1] = True
    a[1000000] = True
    hold = 0
    for i in xrange(1, len(a)):
        if not a[i]:
            hold+=1
            a[i] = hold
        else:
            a[i] = hold
    x = input()
    for i in range(x):
        num1, num2 = map(int, raw_input().split())
        if num1 == 1:
            print a[num2-1]
        elif num1 == 0:
            print a[num2-1]
        else:
            print a[num2-1
                    ]-a[num1-1]
main()
