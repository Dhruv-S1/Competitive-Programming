alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vol = ["a", "e", "i", "o", "u"]
new = []
i = 0
min1 = 0

x = raw_input()

while True:
    if x[i] not in vol:
        new.append(x[i])
        min1 = 999
        for j in range(len(vol)):
            if abs(alp.index(vol[j]) - alp.index(x[i]))<min1 and not(abs(alp.index(vol[j]) - alp.index(x[i]) == min1)):
                current = vol[j]
                min1 = abs(alp.index(vol[j]) - alp.index(x[i]))

        new.append(current)
        current = ""

        if x[i] != "z":
            for j in range((alp.index(x[i])+1), len(alp)):
                if alp[j] not in vol:
                    new.append(alp[j])
                    break
        if x[i] == "z":
            new.append("z")

    else:
        new.append(x[i])


    i = i+1

    if i == len(x):
        break

        
print(''.join(new))
