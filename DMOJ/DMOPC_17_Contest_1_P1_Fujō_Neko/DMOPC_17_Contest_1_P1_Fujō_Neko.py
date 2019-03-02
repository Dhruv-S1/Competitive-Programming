import sys
def main():
    num1, num2 = map(int, sys.stdin.readline().split())
    row = {}
    col = {}
    for i in xrange(1, num1+1):
        row[i] = 0
    for i in xrange(1, num2+1):
        col[i] = 0
    for i in xrange(1, num1+1):
        temp= []
        temp =  sys.stdin.readline()
        for j in xrange(1, len(temp)+1):
            if temp[j-1] == "X":
                row[i] = 1
                col[j] = 1
    
    q = input()
    for i in xrange(q):
        num1, num2 = map(int, sys.stdin.readline().split())
        if col[num1] == 1 or row[num2] == 1:
            print "Y"
        else:
            print "N"
main()
