import sys
x = input()
r = input()
c = input()
d = {}
prevfloor = ''
room = set()
for i in range(r):
  for j in range(c):
    d[(i, j)] = []
for i in range(r):
    floor =''
    floor = raw_input()
    for j in range(len(floor)-1):
        if floor[j] == ".":
            room.add((i, j))
            if floor[j+1] == ".":
                d[(i, j)].append((i, j+1))
                d[(i, j+1)].append((i, j))
                room.add((i, j+1))
    if floor[len(floor)-1] == ".":
        room.add((i, len(floor)-1))
    if i != 0:
        for j in range(len(prevfloor)):
            if prevfloor[j] == ".":
                if floor[j] == ".": 
                    d[(i, j)].append((i-1, j))
                    d[(i-1, j)].append((i, j))

    prevfloor = floor
total = []
totalcount = 0
while True:
    start = room.pop()
    place = [start]
    newplace = []
    count = 0
    while True:
        for i in range(len(place)):
            for j in range(len(d[place[i]])):
                if d[place[i]][j] in room:
                    newplace.append(d[place[i]][j])
                    count+=1
                    room.remove(d[place[i]][j])
        if len(newplace) == 0:
            break
        place = []
        place = newplace
        newplace = []
    total.append(count+1)
    totalcount+=1
    if len(room) == 0:
        break
total.sort()
total.reverse()
rooms1 = 0
hold = 0
for i in range(len(total)):
    if hold+total[i] >x:
        if rooms1 == 1:
            print ("%d room, %d square metre(s) left over") % (rooms1, abs(x-hold))
        else:
            print ("%d rooms, %d square metre(s) left over") % (rooms1, abs(x-hold))
        sys.exit()
    hold+=total[i]
    rooms1 +=1
print ("%d rooms, %d square metre(s) left over") % (rooms1, abs(x-hold))
