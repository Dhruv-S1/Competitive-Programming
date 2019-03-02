import sys
n, m = map(int, raw_input().split())

d = {}
for i in range(m):
    num1, num2 = map(int, sys.stdin.readline().split())
    string = sys.stdin.readline().strip()
    if num2 not in d:
        d[num2] = []
        d[num2].append(string)
    else:
        d[num2].append(string)

you = input()
if you in d:
    for i in range(len(d[you])):
        print d[you][i]
