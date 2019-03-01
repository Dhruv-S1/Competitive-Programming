x = input()
y = input()
red = 0
while True:
    red = 0
    u = min(x, y)
    for i in range(2, u+1):
        if x%i == 0 and y%i == 0:
            x = x/i
            y = y/i
            red = 1
            break
    if red == 0:
        break
    



if x>y and y!=1:
    print("%d %d/%d") % (x//y, x - (y*(x//y)), y)

elif y == 1:
    print(x)
elif x == 0:
    print("0")

else:
    print("%d/%d") % (x ,y)
