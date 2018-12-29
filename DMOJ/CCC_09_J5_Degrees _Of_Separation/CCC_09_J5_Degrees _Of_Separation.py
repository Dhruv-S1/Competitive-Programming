d = {1:set([6]), 2:set([6]), 3:set([6, 4, 15, 5]), 4:set([3, 6, 5]), 5:set([6, 4, 3]), 6:set([2, 1, 3, 4, 5, 7]), 7:set([6, 8]), 8:set([7, 9]), 9:set([8, 10, 12]), 10:set([9, 11]), 11:set([10, 12]), 12:set([9, 11, 13]), 13:set([15, 12, 14]), 14:set([13]), 15:set([3, 13]), 16:set([18, 17]), 17:set([16, 18]), 18:set([16, 17])}

while True:
    y = raw_input()
    if y == "i":
        num1 = input()
        num2 = input()
        if num1 not in d:
            d[num1] = set()
        if num2 not in d:
            d[num2] = set()
        d[num1].add(num2)
        d[num2].add(num1)


    if y == "d":
        num1 = input()
        num2 = input()
        d[num1].remove(num2)
        d[num2].remove(num1)

    if y ==  "n":
        num1 = input()
        print(len(d[num1]))


    if y == "f":
        x = input()
        temp = []
        temp1 = []
        count = 0
        count1 = 0
        vis5 = set()
        temp = list(d[x])
        for i in range(len(temp)):
            temp1 = list(d[temp[i]])
            for j in range(len(temp1)):
                if temp1[j] not in d[x] and temp1[j] != x and temp1[j] not in vis5:
                    count = count+1
                    vis5.add(temp1[j])
                    
        print(count)

            



    if y == "s":
        num1 = input()
        num2 = input()
        temp = []
        temp1 = []
        temp2 = []
        vis = set()
        temp = [num1]
        vis.add(num1)
        count = 0
        while True:
            for i in range(len(temp)):
                temp1 = list(d[temp[i]])
                for j in range(len(temp1)):
                    if temp1[j] not in vis:
                        temp2.append(temp1[j])
                        vis.add(temp1[j])
            count = count+1
            if num2 in vis:
                print(count)
                break
            if temp2 == []:
                print("Not connected")
                break
            temp = []
            temp = temp2
            temp2 = []

            

    if y == "q":
        break
