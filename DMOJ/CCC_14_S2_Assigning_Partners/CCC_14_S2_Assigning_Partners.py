x = input()
a = []
b = []
condition = 0
name1 = 0
name2 = 0
y = raw_input()
h = y.split()
for i in range(len(h)):
    a.append(h[i])

z = raw_input()
h = z.split()
for i in range(len(h)):
    b.append(h[i])
    

for i in range(x):
    for j in range(x):
        name1 = a[i]
        name2 = b[i]
        if b[j] == name1 and a[j] == name2 and j !=i:
            condition = "good"
            break
        else:
            condition = "bad"
            
    if condition != "good":
        condition = "bad"
        break
        
            
print(condition)
