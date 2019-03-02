x = input()
a = []
a = map(int, raw_input().split())
a.sort()
min1 = 999999999999
for i in xrange(len(a)-1):
    if abs(a[i]-a[i+1])<min1:
        min1 = abs(a[i]-a[i+1])
print min1
