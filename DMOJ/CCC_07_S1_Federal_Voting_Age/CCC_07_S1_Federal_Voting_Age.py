x = input()
for i in range(x):
    y = raw_input()
    year, month, day = map(int, y.split())
    if 2007 - year <18:
        print("No")
        continue
    if 2007 - year>18:
        print("Yes")
        continue
    if 2007 - year == 18:
        if month>2:
            print("No")
        if month<2:
            print("Yes")
            continue
        if month == 2:
            if day > 27:
                print("No")
                continue
            else:
                print("Yes")
                continue
