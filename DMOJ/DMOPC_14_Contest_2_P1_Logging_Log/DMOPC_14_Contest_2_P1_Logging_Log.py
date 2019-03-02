x = input()
for i in range(x):
    y = input()
    count = 0
    for j in range(y):
        count = count+input()
    if count == 0:
        print("Weekend")
    else:
        print("Day %d: %d")%(i+1, count)
