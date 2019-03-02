for g in range(10):
    y = ""
    d = {}
    d["red"] = 0
    d["blue"] = 0
    d["green"] = 0
    d["yellow"] = 0
    d["pink"] = 0
    d["violet"] = 0
    d["brown"] = 0
    d["orange"] = 0
    while y != "end of box":
        y = raw_input()
        if y == "end of box":
            break
        d[y] +=1
    count= 0
    for key in d:
        if key != "red":
            if d[key]%7 == 0:
                count+= 13*d[key]/7
            else:
                count +=13*(d[key]/7 + 1)
    count+= 16*d["red"]
    print count
