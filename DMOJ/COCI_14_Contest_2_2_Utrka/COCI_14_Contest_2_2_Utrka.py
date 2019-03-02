x = input()
d = {}
def main():
    for i in xrange(x*2-1):
      y = raw_input()
      if y not in d:
        d[y] = 1  
      else:
        d[y] +=1  
    for key in d:
      if d[key]%2 !=0:
        print key
        break
main()
