x = input()
a = []
for i in range(x+1):
    a.append(1)

for i in range(1, x):
    y = input()
    a[y] = a[y]*(1+a[i])
print(a[y])
