x = input()
k = input()
total = 0
for i in range(k):
    t = input()
    if t == 1:
        total+=30
    elif t == 2:
        total+=60
    else:
        total +=300
if total>x*60:
    print "Return"
else:
    print "Continue"
