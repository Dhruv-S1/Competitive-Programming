x = input()

min1 = 1
max1 =0
count = 0
count1 = 0
while True:
    count = count+1
    min1 = (count-1) + min1
    max1 = count + max1

    if min1<=x and max1>=x:
        print((max1)*(max1+1)/2 - (min1-1)*(min1)/2)
        break
