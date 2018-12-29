node1 = []
x = input()
d = {}
dis = []
for i in range(x):
    dis.append(0)

for i in range(x):
    d[i+1] = []
dis[0] = 0
while True:
    y = raw_input()
    if y == "0 0":
        break
    num1, num2 = map(int, y.split())
    d[num2].append(num1)

fin = set()
def slide(root, node, node1):
    global dis

    if root == 1:
        return 1
    if dis[root-1] != 0 and root in fin:
        return dis[root-1]
    

    node = node+1
    for i in range(len(d[root])):
        dis[root-1] += slide(d[root][i], node, node1)
    fin.add(root)
    return dis[root-1]


slide(x, 0, node1)
print(dis[x-1])
