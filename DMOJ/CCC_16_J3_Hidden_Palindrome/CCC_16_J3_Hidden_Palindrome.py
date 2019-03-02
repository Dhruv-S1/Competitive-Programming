x = raw_input()
a = []
k = []
length = []

for i in range(len(x)):
    for j in range(i, len(x)):
        a.append(x[(i):(j+1)])

for h in range(len(a)):
    if a[h] == a[h][::-1]:
        k.append(a[h])

for b in range(len(k)):
    length.append(len(k[b]))

length.sort()
length.reverse()
print(length[0])
