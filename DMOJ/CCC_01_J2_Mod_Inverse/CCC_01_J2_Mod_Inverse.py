x = input()
y = input()
count = 0
for i in range(1, y):
    if (x*i)%y == 1:
        print(i)
        count = 1
        break
if count == 0:
    print("No such integer exists.")
