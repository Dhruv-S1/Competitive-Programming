import sys
n, k ,q = map(int, raw_input().split())
temp = [int(x) for x in raw_input().split(' ')]
prefix =[]
count = 0


#NOTE this partial solution yeilds 30/100 points

for i in xrange(len(temp)):
    count+=temp[i]
    prefix.append(count)

for j in range(q):
    a, b, x, y = map(int, sys.stdin.readline().split())
    marker = 0
    marker1 = 0
    marker2 = 0
    if x != 1:
        if (prefix[y-1]-prefix[x-2])>k:
            marker = 1
    elif prefix[y-1]>k:
        marker = 1

    temp1 = temp[x-1:y]
    temp1.sort()
    start = 0
    end = len(temp1)-1
    while True:
        if end-start == 0:
            if temp1[end] == a:
                marker1 = 1
            else:
                break
        if end-start == 1:
            if temp1[end] == a or temp1[start] == a:
                marker1 = 1
                break
            break
        if temp1[(start+end)/2] == a:
            marker1 = 1
            break
        if temp1[(start+end)/2] > a:
            end = (start+end)/2
            continue
        if temp1[(start+end)/2] < a:
            start = (start+end)/2
            continue
    start = 0
    end = len(temp1)-1
    while True:
        if end-start == 0:
            if temp1[end] == b:
                marker2 = 1
            else:
                marker2 =0
                break
        if end-start == 1:
            if temp1[end] == b or temp1[start] == b:
                marker2 = 1
                break
            break
        if temp1[(start+end)/2] == b:
            marker2 = 1
            break
        if temp1[(start+end)/2] > b:
            end = (start+end)/2
            continue
        if temp1[(start+end)/2] < b:
            start = (start+end)/2
            continue
    if marker1 and marker2 and marker:
        print("Yes")
    else:
        print("No")
