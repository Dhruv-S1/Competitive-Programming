j = raw_input()
x, y = j.split()

x = int(x)
y = int(y)
marker1 = 0
marker2 = 0
x1 = 0
y1 = 0
while True:
    marker1 = 0
    marker2 = 0
    k = raw_input()
    c, d = k.split()
    c = int(c)
    d = int(d)

    if c == 0 and d == 0:
        break


    x1 = x1 + c
    y1 = y1 + d
    if x1>x:
        x1 = x
    if x1<0:
        x1 = 0
    if y1>y:
        y1 = y
    if y1<0:
        y1 = 0
    print("%d %d") % (x1, y1)
