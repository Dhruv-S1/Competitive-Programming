from itertools import cycle
while True:
    temp = []
    temp = map(int, raw_input().split())
    temp.pop(0)
    if temp == []:
        break
    if len(temp) == 1:
        print(0)
    a = []
    for i in range(len(temp)-1):
        a.append(temp[i+1]-temp[i])
    j = 0
    for i in range(len(a)):
        marker = 0
        temp1 = a[0:i+1]
        j = i+1
        count = 0
        if len(temp1) == len(a):
            print (len(a))
            break
        while True:
            if temp1[count] == a[j]:
                count = (count+1)%len(temp)
                if count % len(temp1) == 0:
                    count = 0
            else:
                marker = 1
                break
            j = j +1
            if j == len(a):
                break
        if marker == 0:
            print(len(temp1))
            break
