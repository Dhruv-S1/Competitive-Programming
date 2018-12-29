x = input()
for i in xrange(x):
    y = input()
    if y >33:
        print 0
    else:
        count = 1
        for j in range(1, y+1):
            count = (count*j)%(2**32)
        print count
