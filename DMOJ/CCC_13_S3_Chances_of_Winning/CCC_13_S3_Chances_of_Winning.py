faveteam = input()
game = input()
temp = []
a = []
b = set()
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(0)
    a.append(temp)
for i in range(game):
    num1, num2, num3, num4 = map(int, raw_input().split())
    b.add((num1, num2))
    b.add((num2, num1))
    if num3> num4:
        a[num1][num2]+=3
    elif num4>num3:
        a[num2][num1] +=3
    else:
        a[num1][num2] +=1
        a[num2][num1] +=1
h = []
def check(a, favteam):
    temp = [0, 0, 0,0, 0]
    for i in range(1, len(a)):
        for j in range(len(a[i])):
            temp[i] += a[i][j]
    count = 0
    for i in range(1, 5):
        if i!= faveteam:
            if temp[i]<temp[faveteam]:
                count+=1
    if count == 3:
        return True
    else:
        return False
            
def recurse(a, team, compete, favteam):
    if compete == 5 or team == 5:
        if team == 5:
            if check(a, faveteam):
                h.append(0)
            return
        recurse(a, team+1, 1, faveteam)
        return
    if team == compete:
        recurse(a, team, compete+1, faveteam)
        return
    else:
        if (team, compete) not in b and (compete, team) not in b:
            a[team][compete] += 3
            b.add((team, compete))
            b.add((compete, team))
            recurse(a, team, compete+1, faveteam)
            a[team][compete]-=3
            a[team][compete]+=0
            a[compete][team] +=3
            recurse(a, team, compete+1, faveteam)
            a[compete][team] -=3
            a[team][compete]+=1
            a[compete][team] +=1
            recurse(a, team, compete+1, faveteam)
            a[team][compete]-=1
            a[compete][team] -=1
            b.remove((team, compete))
            b.remove((compete, team))
        else:
            recurse(a, team, compete+1, faveteam)
            
    return
recurse(a, 1, 2, faveteam)
print len(h)
