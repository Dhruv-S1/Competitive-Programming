import sys
def main():
    n, q = map(int, raw_input().split())
    d = {}
    
    def bfs(d, start, end):
        vis = set()
        new = []
        old = [start]
        marker = 0
        while True:
            for i in range(len(old)):
                for j in xrange(len(d[old[i]])):
                    if d[old[i]][j] not in vis:
                        new.append(d[old[i]][j])
                        vis.add(d[old[i]][j])
            if len(new) == 0:
                break
            if end in vis:
                marker = 1
                break
            old = []
            old = new
            new = []
        if marker == 1:
            return True
        else:
            return False
            
    
    
    d = {}
    for i in xrange(1, n+1):
        d[i] = []
    for i in xrange(q):
        temp = []
        temp = map(str, sys.stdin.readline().split())
        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        if temp[0] == "A":
            d[temp[1]].append(temp[2])
            d[temp[2]].append(temp[1])
        if temp[0] == "Q":
            if bfs(d, temp[1], temp[2]):
                print "Y"
            else:
                print "N"
main()
