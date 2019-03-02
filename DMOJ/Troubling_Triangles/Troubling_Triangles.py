from math import sqrt
import sys
def main():
    for i in range(input()):
      g = map(int, sys.stdin.readline().split())
      num = g[0:2]
      num1 = g[2:4]
      num2 =g[4:6]
      a = sqrt((num[0]-num1[0])**2+(num[1]-num1[1])**2)
      b = sqrt((num[0]-num2[0])**2+(num[1]-num2[1])**2)
      c = sqrt((num1[0]-num2[0])**2+(num1[1]-num2[1])**2)
      s = (a+b+c)/2.0
      print sqrt(s*(s-a)*(s-b)*(s-c)),
      print a+b+c
main()
