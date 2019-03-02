x = input()
temp = []
temp = map(int, raw_input().split())
temp.sort()
if len(temp)%2 == 0:
    x1 = (len(temp)-2)/2
    y1 = (len(temp)+1)/2
else:
    x1 = len(temp)/2
    y1 = (len(temp)/2)+1
if len(temp) == 1:
    print(temp[0])
else:
    while True:
        print(temp[x1]),
        print(temp[y1]),
        x1 = x1-1
        y1 = y1+1
        if y1 == len(temp):
            break
    if len(temp)%2 == 1:
        print(temp[0])
