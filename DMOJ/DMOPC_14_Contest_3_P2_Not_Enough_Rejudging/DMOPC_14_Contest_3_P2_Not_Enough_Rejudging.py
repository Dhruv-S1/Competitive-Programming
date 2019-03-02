def main():
    x = input()
    a = []
    for i in range(x):
        a.append(raw_input())
    WA = a.count("WA")
    AC = a.count("AC")
    IR = a.count("IR")
    TLE = a.count("TLE")
    wacount = 0
    ircount = 0
    WA = 0.3*WA
    for i in xrange(len(a)):
        if a[i] == "AC":
            print "AC"
        if a[i] == "TLE":
            print "WA"
        if a[i] == "WA":
            wacount+=1
            if wacount<=WA:
                print "AC"
            else:
                print "WA"
        if a[i] == "IR":
            ircount+=1
            if ircount<=10:
                print "AC"
            elif ircount>10 and ircount<=20:
                print "WA"
            else:
                print "IR"
main()
