def main():
    x = input()
    y = raw_input()
    a = []
    prev = 0
    b = ''
    for i in range(len(y)):
        if y[i] == "O":
            b +="O"
        else:
            if b!= '':
                a.append(b)
            b = ''
    if len(b) != 0:
        a.append(b)
    print len(a)
    for i in range(len(a)):
        print a[i]
main()
