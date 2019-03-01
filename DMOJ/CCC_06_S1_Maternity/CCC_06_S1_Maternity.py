d = {1:[], 2:[], 3:[], 4:[], 5:[]}

y = raw_input()
x = raw_input()
z = input()
for i in range(1, 10, 2):
    for j in range(2):
        for k in range(2):
            if y[i-1:i+1][j] == x[i-1:i+1][k]:
                d[(i+1)/2].append(y[i-1:i+1][j])
            else:
                if y[i-1:i+1][j].isupper():
                    d[(i+1)/2].append(y[i-1:i+1][j])
                else:
                    d[(i+1)/2].append(x[i-1:i+1][k])
                    
                
for i in range(z):
    y = raw_input()
    marker = 0
    for j in range(len(y)):
        if y[j] in d[j+1]:
            continue
        else:
            print("Not their baby!")
            marker = 1
            break
    if marker == 0:
        print("Possible baby.")
