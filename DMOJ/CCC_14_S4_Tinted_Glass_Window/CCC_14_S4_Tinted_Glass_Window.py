import sys
def main():
    n = input()
    t = input()
    a = []
    d = {}
    ycompress = set()
    rect = []
    for i in range(n):
        x1, y1, x2, y2, tint  = map(int, sys.stdin.readline().split())
        rect.append((x1, y1, y2, tint))
        rect.append((x2, y1, y2, -tint)) #used so tint doesnt carry on hence a negative tint
        ycompress.add(y1)
        ycompress.add(y2)
    ycompress = list(ycompress)
    ycompress.sort()
    y = []
    rect.sort()
    for i in range(len(ycompress)):
        d[ycompress[i]] = i+1
    for j in range(len(ycompress)+1):
        y.append(0)
    covered = 0
    ycompress = [-1]+ycompress
    rect = [1]+rect
    
    for i in range(1, len(rect)):
        for j in range(1, len(y)):
            if y[j] >= t:
                covered += (ycompress[j+1] - ycompress[j])*(rect[i][0] - rect[i-1][0])
        for k in range(d[rect[i][1]], d[rect[i][2]]):
            y[k] += rect[i][3]
    
    print covered
main()
