a = []
b = []
c = []
d = []
q = 0
w = 0
e = 0
r = 0
t = 0
y = 0
u = 0
i = 0

x = raw_input()
a = x.split()

for i in range(4):
    a[i] = int(a[i])

x = raw_input()
b = x.split()

for i in range(4):
    b[i] = int(b[i])

x = raw_input()
c = x.split()

for i in range(4):
    c[i] = int(c[i])
    
x = raw_input()
d = x.split()

for i in range(4):
    d[i] = int(d[i])

for i in range(4):
    q += a[i]
    w += b[i]
    e += c[i]
    r += d[i]


t = a[1] + b[1] + c[1] + d[1]
y = a[2] + b[2] + c[2] + d[2]
u = a[3] + b[3] + c[3] + d[3]
i = a[0] + b[0] + c[0] + d[0]

if t == y == u == i == q == w == e == r:
    print("magic")

else:
    print("not magic")
