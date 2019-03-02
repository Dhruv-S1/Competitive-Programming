x = raw_input()
y = raw_input()
d = {"a": 25, "b": 24, "c":23, "d": 22, "e": 21, "f": 20, "g":19, "h": 18, "i": 17, "j":16, "k": 15, "l": 14, "m": 13, "n": 12, "o": 11, "p":10, "q": 9, "r": 8, "s": 7, "t": 6, "u": 5, "v": 4, "w": 3, "x": 2, "y":1, "z": 0}
alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alp.reverse()
count = 0
while True:
    new = ''
    if y in x:
        print count
        count
        print x
        break
    for i in range(len(x)):
        new = new+alp[(d[x[i]]+1)%26]
    count = count+1
    x = ''
    x = new
