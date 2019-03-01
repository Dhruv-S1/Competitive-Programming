from math import sqrt
def main():
    x = input()
    y = input()
    count1 = 0
    for i in range(x, y+1):
      count = 0
      for j in range(1, int(i/2)+2):
        if i%j == 0:
          count+=1
      if count+1 == 4:
        count1 +=1
    print "The number of RSA numbers between %d and %d is %d" % (x, y, count1)
main()
