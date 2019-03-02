import sys
x = int(sys.stdin.readline())
count = 0
while True:
    count += 1
    if count>x:
        break
    y = int(sys.stdin.readline())
    if y == 0:
        print("F")
    elif y &(y-1) == 0:
        print("T")
    else:
        print("F")
