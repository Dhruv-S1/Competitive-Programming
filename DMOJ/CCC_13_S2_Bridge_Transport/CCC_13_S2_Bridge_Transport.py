import sys
def main():
    a = input()
    b = input()
    c = []
    d = []
    sum1 = 0
    j = 0
    counter = 0
    for i in xrange(b):
        c.append(int(sys.stdin.readline()))
    for i in xrange(b):
        counter = 0
        d.append(c[i])
        h = len(d)
        j = j+1
        for k in range(h):
            counter = counter + d[k]
            
        if counter> a:
            j = j-1
            break
        if j == len(c):
            break
        if h==4:
            d.pop(0)
            
    print(j)
main()
