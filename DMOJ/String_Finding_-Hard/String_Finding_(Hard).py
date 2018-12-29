import sys
def main():
    i = 0
    j = 0
    wholestring = sys.stdin.readline().strip()
    string = sys.stdin.readline().strip()
    if len(string) == 1:
        print wholestring.index(string)
        sys.exit()
    a = []
    for i in range(len(string)):
        a.append(0)
    
    i = 1
    j = 0
    while True:
        if j == 0:
            if string[j] == string[i]:
                a[i] = j+1
                if i == len(a)-1:
                    break
                i+=1
                j+=1
                continue
            if string[j] != string[i]:
                if i == len(a)-1:
                    break
                i+=1
        else:
            if string[j] == string[i]:
                a[i] = j+1
                if i == len(a)-1:
                    break
                i+=1
                j+=1
            if string[j]!=string[i]:
                j = a[j-1]
                if i == len(a)-1 and j == 0:
                    break
                continue
    i = 0
    j = 0
    while True:
        if i>len(wholestring)-1:
            break
        if j == 0:
            if string[j] == wholestring[i]:
                j+=1
                i+=1
                continue
            if string[j]!=wholestring[i]:
                i+=1
        else:
            if string[j] == wholestring[i]:
                if j == len(string)-1:
                    print i-(len(string)-1)
                    sys.exit()
                j+=1
                i+=1
                continue
            if string[j]!=wholestring[i]:
                j = a[j-1]
            
        
    print -1
main()
