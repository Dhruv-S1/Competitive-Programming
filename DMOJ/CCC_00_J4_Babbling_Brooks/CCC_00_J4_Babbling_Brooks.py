x = input()
a = []
for i in range(x):
    a.append(float(input()))

while True:
    x = input()
    if x == 99:
        y = input()
        z = input()
        temp = []
        for i in range(len(a)):
            if i+1 == y:
                temp.append((float(z)/float(100))*a[i])
                temp.append(a[i] - (float(z)/float(100))*a[i])

            else:
                temp.append(a[i])
        a = []
        a = temp
        temp = []
    if x == 88:
        temp = []
        y = input()
        for i in range(len(a)):
            if i+1 == y:
                temp.append(a[i]+a[i+1])
            elif i+1 == y+1:
                continue
            else:
                temp.append(a[i])
        a = []
        a = temp
        temp = []
    if x == 77:
        break

for i in range(len(a)):
    print(int(round(a[i]))),
