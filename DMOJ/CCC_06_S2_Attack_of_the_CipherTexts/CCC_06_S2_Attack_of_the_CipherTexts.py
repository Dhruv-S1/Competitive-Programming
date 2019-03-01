x = raw_input()
y = raw_input()
z = raw_input()
d = {}
c = ""
for i in range(len(x)):
    d[y[i]] = x[i]

for i in range(len(z)):
    if z[i] in d:
        c = c + d[z[i]]
    else:
        c = c+"."

print(c)
