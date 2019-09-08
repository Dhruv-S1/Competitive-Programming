# Problem can be found at https://leetcode.com/problems/string-to-integer-atoi/
class Solution(object):
    def myAtoi(self, str):
        def check(s):
            if(s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s =="7" or s =="8" or s =="9" or s =="0"):
                return True
            else:
                return False
        x1 = ""
        current = 0
        negcheck = 0
        pos = 0
        numon = 0
        for i in range(len(str)):
            if(numon == 1 and not check(str[i])):
                return 0
            if(str[i] == "0"):
                numon = 1
            if(str[i] == " " or str[i] == "0"):
                current+=1
                continue
            if (str[i] == "-" and pos==0):
                numon = 1
                negcheck=1
                current = i+1
                continue
            if(str[i] == "+" and negcheck ==0):
                numon= 1
                current = i+1
                pos = 1
                continue
            if(check(str[i])):
                current = i
                break
            else:
                return 0
        if(negcheck == 1 and not check(str[i])):
           return 0

        for i in range(current, len(str)):
            if(check(str[i])):
                x1+=str[i]
            else:
                break
        if(x1 == "" or x1=="-"):
            return 0
        if(int(x1)>=2147483647 and negcheck == 0):
            return 2147483647
        if(int(x1)> 2147483648 and negcheck==1):
            return -2147483648
        if(negcheck==1):
            return "-" + x1
        else:
            return x1
            
        
                
            
        
