x = input()
count = 0
for i in range((x-3)):
    for g in range((i+1), (x-2)):
        for h in range((g+1), (x-1)):
            count = count +1

print(count)
