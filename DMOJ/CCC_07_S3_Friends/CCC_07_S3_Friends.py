x = input()
d = {}
a = []
for i in range(x):
    y = raw_input()

    num1, num2 = y.split()
    d[num1] = num2

while True:
    counter = 0
    marker = 0
    a = []
    x = raw_input()
    num1, num2 = x.split()
    if num1 == "0" and num2 == "0":
        break
    num3 = num1
    while True:
        num3 = d[num3]
        if num3 == num1:
            break
        a.append(num3)
        if num3 != num2:
            counter = counter  + 1
        if num3 == num2:
            marker = 1
            break
    if marker != 1:
        print("No")
    else:
        print("Yes %d") % (counter)
