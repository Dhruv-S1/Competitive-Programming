x = input()
# NOTE this partial solution yields only 50/100 points.

for i in range(x):
    a = set()
    y = raw_input()
    for i in range(len(y)):
        for j in range(i, len(y)):
                a.add(y[i:(j+1)])
    print(len(a) + 1)
