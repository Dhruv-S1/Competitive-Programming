x = input()
b = []
a = []
b.append(0)
for i in range(x):
    b.append(999999999)

y = input()
for i in range(y):
    a.append(input())

a.sort()
for i in range(y):
    for j in range(1, x+1):
        if j>=a[i]:
            b[j] = min(b[j-a[i]] + 1, b[j]) 
        

if b[len(b)-1] == 999999999:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in %d strokes.") % b[len(b)-1]
