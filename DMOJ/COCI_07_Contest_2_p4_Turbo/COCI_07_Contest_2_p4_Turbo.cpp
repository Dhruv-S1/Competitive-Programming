import sys
def main():
    x = input()
    bittree = []
    bittree1 = []
    for i in xrange(x+1):
        bittree.append(0)
        bittree1.append(0)
    
    def add(bittreea, i):
        sum1 = 0
        while i>0:
            sum1+=bittreea[i]
            i -=i&(-i)
        return sum1
    
    def update(bittreea, i, n):
        while i<=n:
            bittreea[i]+=1
            i+=i&(-i)
    initialpositions = []
    for i in xrange(x+1):
        initialpositions.append(0)
    for i in xrange(x):
        y = int(sys.stdin.readline())
        initialpositions[y] = i+1
    total = 0
    n = 1
    m = x
    while True:
        hold = add(bittree, x)-add(bittree, initialpositions[n]-1)
        hold1 = add(bittree1, initialpositions[n]-1)
        total +=abs(n-(hold-hold1+initialpositions[n]))
        print abs(n-(hold-hold1+initialpositions[n]))
        update(bittree, initialpositions[n], x)
        n+=1
        if n>=m:
            break
        hold = add(bittree, x)-add(bittree, initialpositions[m]-1)
        hold1 = add(bittree1, initialpositions[m]-1)
        total +=abs(m-(hold-hold1+initialpositions[m]))
        print abs(m-(hold-hold1+initialpositions[m]))
        update(bittree1, initialpositions[m], x)
        m-=1
        if m<=n:
            break
    print 0
main()
