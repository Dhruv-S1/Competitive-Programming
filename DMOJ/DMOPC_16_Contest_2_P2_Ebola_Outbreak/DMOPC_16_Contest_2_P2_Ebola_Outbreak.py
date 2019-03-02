#NOTE this partial solution yields 80/100 points
x = raw_input()
n,m = map(int, x.split())
b = set()
b.add(1)
marker = 0
z = set()
for i in range(m):
    y = map(int, raw_input().split())
    z = set(y[1:y[0]+1])
    for key in b:
        if key in z:
            marker = 1
    if marker == 1:
        b = b|z
    marker = 0


print(len(b))
b = list(b)
b.sort()
print(' '.join(str(e) for e in b))
