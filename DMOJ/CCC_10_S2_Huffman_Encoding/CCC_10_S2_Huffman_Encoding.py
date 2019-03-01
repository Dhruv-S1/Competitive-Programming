x = input()
a = []
r = 0
n = ""
for i in range(x):
    y = raw_input()
    h = y.replace(" ","")
    a.append(h)
h = raw_input()
while(r != len(h)):
    for i in range(len(a)):
        b = a[i][1:]
        if b == h[r: (r +len(a[i][1:]))]:
            n = n + a[i][0] 
            r = r + len(a[i][1:])
print(n)
