m = input()
n = input()
a = []
b= []
for i in range(n):
    a.append(raw_input())
for i in range(n):
    b.append(raw_input())
array = []
for i in range(m+1):
    array.append(0)

global m
count1 = 0
def recurse(A, B, count):
    global count1
    count= count+1
    C = ""
    D = ""
    C = A
    D = B
    if A == B and A != "":
        count1 = count-1
        return True
    if count>m:
        return False
        
    for i in range(len(a)):
        A = A+a[i]
        B = B+b[i]
        array[count-1] = i+1
        if recurse(A, B, count):
            return True
        A = C
        B = D
        
if recurse("", "", 0) is None:
    print ("No solution.")
else:
    print(count1)
    for i in range(count1):
        print(array[i])
