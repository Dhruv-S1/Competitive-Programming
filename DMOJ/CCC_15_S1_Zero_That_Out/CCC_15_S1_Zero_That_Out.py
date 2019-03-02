x = input()
tot = []

for i in range(x):
    y = input()
    if y == 0:
        tot.pop(len(tot)-1)
    else:
        tot.append(y)

print(sum(tot))
