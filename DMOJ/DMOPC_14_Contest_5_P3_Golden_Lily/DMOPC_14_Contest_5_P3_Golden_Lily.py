def main():
    L, D = map(int, raw_input().split())
    a = []
    minarray = []
    for i in range(D):
        temp = []
        temp = map(int, raw_input().split())
        a.append(temp)
    for i in range(D):
        temp = []
        for j in range(L):
            temp.append(0)
        minarray.append(temp)
    minarray[0][0] = a[0][0]
    x1, y1 = map(int, raw_input().split())
    for i in range(D):
        for j in range(L):
            if i != 0 and j!= 0:
                minarray[i][j] = min(minarray[i-1][j]+a[i][j], minarray[i][j-1]+a[i][j])
            elif i == 0 and j!=0:
                minarray[i][j] = minarray[i][j-1]+a[i][j]
            elif j == 0 and i!=0:
                minarray[i][j] = minarray[i-1][j]+a[i][j]
        if i!= 0:
            for j in range(L-1, 0, -1):
                if j!= L-1:
                    minarray[i][j] = min(minarray[i][j], minarray[i-1][j]+a[i][j], minarray[i][j+1]+a[i][j])
                else:
                    minarray[i][j] = min(minarray[i][j], minarray[i-1][j]+a[i][j])
                
    print minarray[y1][x1]
main()
