def main():
    n, x = map(int, raw_input().split())
    a = []
    primes = []
    for i in xrange(n+1):
        a.append(True)
    a[1] = False
    count = 1
    while count**2<=n:
        if a[count]:
            for i in xrange(count*2, n+1, count):
                a[i] = False
    
        count +=1
    for i in xrange(1, len(a)):
        if a[i]:
            primes.append(i)
    count = 0
    for i in xrange(len(primes)):
        count+=(n-primes[i])/x
        if primes[i]!=n:
           count+=(n-1-primes[i])/x 
    if a[n]:
        print count+len(primes)*2-1
    else:
        print count+len(primes)*2
main()
