hold = ''
x = []
hold =  raw_input()
for i in range(len(hold)):
    x.append(hold[i])
original = ''
for i in range(len(x)):
    original = original+x[i]
original = int(original)
y = []
for i in range(len(x)):
    y.append(x[i])
hold = 0
num1 = ''
num2 = ''
for i in xrange(1, len(x)):
    if ((int(x[i])%2) == (int(x[i-1])%2)):
        hold = i
        if int(x[i])%2 == 0:
            if int(x[i]) == 0:
                x[i] = '1'
                count = i+1
                mod = 0
                while count<len(x):
                    if mod == 0:
                        x[count] = '0'
                    else:
                        x[count] = '1'
                    count+=1
                    mod = (mod+1)%2
                for j in range(len(x)):
                    num1 = num1+x[j]
                num1 = int(num1)
                print num1
                break   
            else:
                x[i] = str(int(x[i])+1)
                y[i] = str(int(x[i])-2)
                count = i+1
                mod = 0
                while count<len(x):
                    if mod == 0:
                        x[count] = '0'
                        y[count] = '8'
                    else:
                        x[count] = '1'
                        y[count] = '9'
                    mod = (mod+1)%2
                    count+=1
                for j in range(len(x)):
                    num1 = num1+x[j]
                for j in range(len(y)):
                    num2 = num2+y[j]
                num1 = int(num1)
                num2 = int(num2)
                if (num1-original)<(original-num2):
                    print num1
                elif (num1-original)==(original-num2):
                    print num2, num1
                else:
                    print num2
                break 
        if int(x[i])%2 == 1:
            if int(x[i]) == 9:
                x[i] = '8'
                count = i+1
                mod = 0
                while count<len(x):
                    if mod == 0:
                        x[count] = '9'
                    else:
                        x[count] = '8'
                    count+=1
                    mod = (mod+1)%2
                for j in range(len(x)):
                    num1 = num1+x[j]
                num1 = int(num1)
                print num1
                break   
            else:
                x[i] = str(int(x[i])+1)
                y[i] = str(int(x[i])-2)
                count = i+1
                mod = 0
                while count<len(x):
                    if mod == 1:
                        x[count] = '0'
                        y[count] = '8'
                    else:
                        x[count] = '1'
                        y[count] = '9'
                    mod = (mod+1)%2
                    count+=1
                num1 = ''
                num2 = ''
                for j in range(len(x)):
                    num1 = num1+x[j]
                for j in range(len(y)):
                    num2 = num2+y[j]
                num1 = int(num1)
                num2 = int(num2)
                
                if (num1-original)<(original-num2):
                    print num1
                elif(num1-original) == (original-num2):
                    print num2, num1
                else:
                    print num2
                break
