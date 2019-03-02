x = input()
y = input()
a = []
count = 0
tot = 0
for i in range(y):
    a.append(input())

a.sort()

for i in range(y):
    tot = tot + a[i]
    if tot>x:
        break
    count = count  +1

print(count)
