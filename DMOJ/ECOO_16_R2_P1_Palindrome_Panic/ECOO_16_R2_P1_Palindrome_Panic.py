# NOTE: This partial solution gives 80/100 points
for i in range(10):
    y = raw_input()
    if y == y[::-1]:
        print(0)
        continue
    sample = ''
    sample = y[::-1]
    count = 0
    j = 0
    k = 0
    while True:
        if y[j] == sample[k]:
            count = count+1
            j = j+1
            k = k+1
        elif k != 0 and sample[k] !=y [j]:
            k = 0
            count = 0
        else:
            j = j+1

        if j==len(y):
            break

    sufmin = len(y) - count
    
    count = 0
    j = 0
    k = 0
    while True:
        if sample[j] ==  y[k]:
            count = count+1
            j = j+1
            k = k+1
        elif k != 0 and y[k] != sample[j]:
            k = 0
            count = 0
        else:
            j = j+1

        if j==len(y):
            break

    print(min(len(y) - count, sufmin))
