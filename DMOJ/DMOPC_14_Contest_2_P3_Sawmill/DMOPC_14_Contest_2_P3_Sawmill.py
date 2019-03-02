x = input()
energy = []
energy = map(int, raw_input().split())
length = map(int, raw_input().split())
energy.sort()
length.sort()
length.reverse()

tot = 0
for i in range(x):
    tot += length[i]*energy[i]
print tot
