old = []
for  i in range(input()):
    temp = map(str, raw_input().split())
    old.append(temp)
for i in range(input()):
    num1, num2 = map(int, raw_input().split())
    min1 = 9999999
    person = ''
    for j in range(len(old)):
        if int(old[j][1])-num1>=0:
            if int(old[j][1])-num1<=num2:
                if int(old[j][1])-num1<min1:
                    person= old[j][0]
                    min1 = int(old[j][1])-num1
    if person == '':
        print "No suitable teacher!"
    else:
        print person
