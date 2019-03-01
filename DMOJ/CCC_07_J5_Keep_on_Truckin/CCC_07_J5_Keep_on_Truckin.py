a = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
mind = input()
maxd = input()
add = input()
b = []
for i in range(add):
    a.append(input())

a.sort()

for i in range(len(a)):
    b.append(0)
b[0] = 1

for i in range(len(a)):
    for j in range(i):
        x = a[i] - mind
        y = a[i] - maxd

        if x>=a[j] and y<=a[j]:
            b[i] = b[i] + b[j]
            

print(b[len(b)-1])
