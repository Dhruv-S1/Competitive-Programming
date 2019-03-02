a= 0
b = 0
j = 0
y = input()
y = y+1
while True:
    for i in range(0, 10):
        if str(y).count(str(i)) > 1:
            j = 0
            break

        else:
            j = 1

    if j == 1:
        break


    y = y+1
    
print(y)
