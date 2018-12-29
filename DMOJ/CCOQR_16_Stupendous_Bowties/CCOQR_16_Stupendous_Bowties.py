import sys
def main():
    x = input()
    dy = {}
    dx = {}
    
    points = []
    pointsy = []
    temp = []
    for i in xrange(x):
        temp = map(int, sys.stdin.readline().split())
        points.append(temp)
    points.sort()
    points[0].append(0)
    count = 0
    for i in xrange(1, len(points)):
        if points[i][0] == points[i-1][0]:
            count+=1
            points[i].append(count)
        else:
            points[i].append(0)
            count = 0
    count = 0
    points[len(points)-1].append(0)
    for i in xrange(len(points)-2, -1, -1):
        if points[i][0] == points[i+1][0]:
            count+=1
            points[i].append(count)
        else:
            points[i].append(0)
            count = 0
    hold = 0
    for i in xrange(len(points)):
        hold = points[i][0]
        points[i][0] = points[i][1]
        points[i][1] = hold
    points.sort()
    points[0].append(0)
    for i in xrange(1, len(points)):
        if points[i][0] == points[i-1][0]:
            count+=1
            points[i].append(count)
        else:
            points[i].append(0)
            count = 0
    count = 0
    points[len(points)-1].append(0)
    for i in xrange(len(points)-2, -1, -1):
        if points[i][0] == points[i+1][0]:
            count+=1
            points[i].append(count)
        else:
            points[i].append(0)
            count = 0
    count = 0
    for i in xrange(len(points)):
        count+= points[i][2]*points[i][3]*points[i][4]*points[i][5]*2
    print count
main()
