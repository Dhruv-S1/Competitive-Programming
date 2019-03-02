a = []

for i in range(6):
    a.append(raw_input())

w = a.count("W")
l = a.count("L")

if w == 5 or w ==6:
    print("1")

if w == 3 or w == 4:
    print("2")

if w == 1 or w == 2:
    print("3")

if w == 0:
    print("-1")
