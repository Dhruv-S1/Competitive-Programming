import sys
from math import sqrt
while True:
  r = int(sys.stdin.readline())
  if r == 0:
    break
  count = 0
  for i in range(1, r):
      count = count + int(sqrt(r**2 - (r-i)**2))

        
  print(count*4+4*r+1)
