x = input()
for i in range(x):
    y = raw_input()
    c,r = map(int, y.split())
    a = []
    for j in range(r):
        temp = []
        y = raw_input()
        for k in range(len(y)):
            temp.append(y[k])
        a.append(temp)
    visit = set()
    current = []
    t = []
    for j in range(r):
        if "C" in a[j]:
            t = a[j].index("C")
            break
    current.append((j, t))
    visit.add(t)
    newcurrent = []
    count = 0
    marker = 0
    while True:
        for j in range(len(current)):
            if current[j][0]-1>=0 and (current[j][0]-1, current[j][1]) not in visit and a[current[j][0]-1][current[j][1]]!="X":
                newcurrent.append((current[j][0]-1, current[j][1]))
                visit.add((current[j][0]-1, current[j][1]))
                if a[current[j][0]-1][current[j][1]] == "W":
                    print(count+1)
                    marker = 1
                    break
            if current[j][0]+1<=r-1 and (current[j][0]+1, current[j][1]) not in visit and a[current[j][0]+1][current[j][1]]!="X":
                newcurrent.append((current[j][0]+1, current[j][1]))
                visit.add((current[j][0]+1, current[j][1]))
                if a[current[j][0]+1][current[j][1]] == "W":
                    print(count+1)
                    marker = 1
                    break
            if current[j][1]-1>=0 and (current[j][0], current[j][1]-1) not in visit and a[current[j][0]][current[j][1]-1] != "X":
                newcurrent.append((current[j][0], current[j][1]-1))
                visit.add((current[j][0], current[j][1]-1))
                if a[current[j][0]][current[j][1]-1] == "W":
                    print(count+1)
                    marker = 1
                    break
            if current[j][1]+1<=c-1 and (current[j][0], current[j][1]+1) not in visit and a[current[j][0]][current[j][1]+1] != "X":
                newcurrent.append((current[j][0], current[j][1]+1))
                visit.add((current[j][0], current[j][1]+1))
                if a[current[j][0]][current[j][1]+1] == "W":
                    print(count+1)
                    marker = 1
                    break
        count = count+1
        if marker == 1:
            break
        if count == 59:
            print("#notworth")
            break
        current = []
        current = newcurrent
        newcurrent = []
