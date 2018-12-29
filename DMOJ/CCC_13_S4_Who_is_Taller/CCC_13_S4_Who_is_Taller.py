import sys
def main(taller, smaller, big):
    temp = [smaller]
    temp1 = []
    while True:
        for i in range(len(temp)):
            for j in xrange(len(big[temp[i]])):
                temp1.append(big[temp[i]][j])
                if big[temp[i]][j] == taller:
                    print"yes"
                    sys.exit()
        if len(temp1) == 0:
            break
        temp = []
        temp = temp1
        temp1 = []
def main1(taller, smaller, big):
    temp = []
    temp = [taller]
    temp1 = []
    while True:
        for i in range(len(temp)):
            for j in xrange(len(big[temp[i]])):
                temp1.append(big[temp[i]][j])
                if big[temp[i]][j] == smaller:
                    print"no"
                    sys.exit()
        if len(temp1) == 0:
            break
        temp = []
        temp = temp1
        temp1 = []
        
n, m = map(int, raw_input().split())
big = {}
for i in xrange(1, n+1):
    big[i] = []
for i in xrange(m):
    num1, num2 = map(int, sys.stdin.readline().split())
    big[num2].append(num1)
taller, smaller = map(int, raw_input().split())

main(taller, smaller, big)
main1(taller, smaller, big)
print "unknown"
