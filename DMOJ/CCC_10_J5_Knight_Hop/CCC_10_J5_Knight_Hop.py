def main():
    x = raw_input()
    y = raw_input()
    start = []
    end = []
    start = map(int, x.split())
    end = map(int, y.split())
    current = []
    current = start
    temp = []
    vis = set()
    count = 0
    new = []
    current = [current]
    while True:
        if start == end:
            print(0)
            break
        for i in range(len(current)):
            x = current[i][0]
            y = current[i][1]
            if x-1 >= 1 and y+2<=8 and (x-1, y+2) not in vis:
                vis.add((x-1, y+2))
                new.append([x-1, y+2])
            if x+1<=8 and y+2<=8 and (x+1, y+2) not in vis:
                vis.add((x+1, y+2))
                new.append([x+1, y+2])
            if x-2>=1 and y+1<=8 and (x-2, y+1) not in vis:
                vis.add((x-2, y+1))
                new.append([x-2, y+1])
            if x+2<=8 and y+1<=8 and (x+2, y+1) not in vis:
                vis.add((x+2, y+1))
                new.append([x+2, y+1])
            if x-2>= 1 and y-1>=1 and (x-2, y-1) not in vis:
                vis.add((x-2, y-1))
                new.append([x-2, y-1])
            if x-1>=1 and y-2>=1 and (x-1, y-2) not in vis:
                vis.add((x-1, y-2))
                new.append([x-1, y-2])
            if x+1<=8 and y-2>=1 and (x+1, y-2) not in vis:
                vis.add((x+1, y-2))
                new.append([x+1, y-2])
            if y-1>=1 and x+2<=8 and (x+2, y-1) not in vis:
                vis.add((x+2, y-1))
                new.append([x+2, y-1])
        count = count+1
        if tuple(end) in vis:
            print(count)
            break
        current = []
        current = new
        new = []
main()
