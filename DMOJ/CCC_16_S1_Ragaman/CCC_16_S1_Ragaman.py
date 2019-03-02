x = raw_input()
y = raw_input()
d = {}
f = {}
ast = 0
diff = 0
alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
a = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
b = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
c = []
for i in range(len(x)):
    a[x[i]] += 1

for i in range(len(y)):
    if y[i] == "*":
        ast = ast + 1
    else:  
        b[y[i]] += 1

for i in range(len(alp)):
    if a[alp[i]] != b[alp[i]]:
        diff += abs(a[alp[i]] - b[alp[i]])

if diff == ast and len(x) == len(y):
    print("A")
else:
    print("N")
