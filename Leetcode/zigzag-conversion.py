class Solution(object):
    def convert(self, s, numRows):
        d= {}
        if(int(numRows) == 1):
            return s
        for i in range(1, int(numRows)+1):
            d[i] = []
        count= 0
        a= []
        add = 1
        sub = 0
        count1 = 0
        print(int(numRows))
        while(True):
            if(add ==1):
                count +=1
            if(sub == 1):
                count-=1
            if(count == (int(numRows)+1)):
                count-=1
                sub = 1
                add = 0
                continue
            if(count == 0):
                add = 1
                sub= 0
                count = 1
                continue
            if(count1==len(s)):
                break
            
            d[count].append(s[count1])
            count1+=1

        ans = ''
        for i in range(1, int(numRows)+1):
            if i in d:
                for j in range(len(d[i])):
                    ans += d[i][j]
        return ans
                
    
    
    
