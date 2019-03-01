import sys
def main():
    n, k, d = map(int, raw_input().split())
    jacks = []
    jacks.append(1)
    for i in xrange(k):
      jacks.append(1)
    jacks.append(1)
    count = 0
    for i in xrange(n):
      y = raw_input()
      if y == "T":
        count+=1
      else:
        hold = int(y[2:])
        if jacks[count]*hold>d or jacks[count] == -1:
            jacks[count] = -1
        else:
            jacks[count] = jacks[count]*hold
    marker = 0
    temp = []
    
    for i in xrange(len(jacks)-2, 0, -1):
        if jacks[i] <0 or marker == 1:
            marker = 1
            temp.append("dust")
            continue
        else:
            jacks[i] = jacks[i+1]*jacks[i]
            if jacks[i]>d:
                marker = 1
                temp.append("dust")
            else:
                temp.append(jacks[i])
    
    
    for i in xrange(len(temp)-1, -1, -1):
        print(temp[i])
main()
