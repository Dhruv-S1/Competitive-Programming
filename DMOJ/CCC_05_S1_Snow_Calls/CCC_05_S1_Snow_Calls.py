d =  {"A":2, "B": 2, "C": 2, "D": 3, "E":3, "F": 3, "G": 4, "H": 4, "I": 4, "J":5, "K":5, "L":5, "M": 6, "N": 6, "O": 6, "P":7, "Q": 7, "R": 7, "S": 7, "T": 8, "U": 8, "V":8, "W":9, "X":9, "Y":9, "Z": 9}
x = input()
for i in range(x):
    y = raw_input()
    b = ["0", "0","0", "0", "0","0","0", "0","0", "0"]
    j = 0
    counter = 0
    while True:
        if y[counter] == "-":
            counter = counter+1
            continue
        if y[counter]  in d:
            b[j] = d[y[counter]]
        else:
            b[j] = y[counter]
            
        counter = counter+1
        j = j+1
        if j==10:
            break
    string = ""
    for k in range(3):
        string = string+str(b[k])
    string = string + "-"
    for k in range(3, 6):
        string = string+str(b[k])
    string = string + "-"
    for k in range(6, 10):
        string = string+str(b[k])
    print(string)
