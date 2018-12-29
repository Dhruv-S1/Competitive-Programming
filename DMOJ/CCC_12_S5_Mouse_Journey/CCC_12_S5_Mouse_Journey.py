a = []
b = []
novalid = []
temp = []
mark1 = 0
mark2 = 0
x = raw_input()
num1, num2 = x.split()
r = int(num1)
c = int(num2)
for i in range(c+1):
    a.append(0)
b.append(a)

y = input()
for j in range(y):
    temp = []
    y = raw_input()
    num1, num2 = y.split()
    num1 = int(num1)
    num2 = int(num2)
    temp.append(num1)
    temp.append(num2)
    novalid.append(temp)

    
for i in range(1, r+1):
    a = []
    a.append(0)
    for j in range(1, c+1):
        temp = []
        temp.append(i)
        temp.append(j)
        if i == 1 and temp not in novalid and mark1 !=1:
            a.append(1)
        elif j == 1 and temp not in novalid and mark2!=1:
            a.append(1)
        else:
            if j == 1:
                mark2 = 1
            if i == 1:
                mark1 = 1
            a.append(0)
    b.append(a)



for i in range(1, r+1):
    for j in range(2, c+1):
        temp = []
        temp.append(i)
        temp.append(j)
        if temp not in novalid:
            b[i][j] = b[i-1][j] +  b[i][j-1]

print(b[r][c])
