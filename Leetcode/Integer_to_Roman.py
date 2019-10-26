class Solution(object):
    def intToRoman(self, num):
        x = str(num)
        ans = ""
        print(x)
        for i in range(len(x)-1, -1, -1):
            print(i)
            b = len(x)-i-1
            if(x[b] == "9"):
                if(i == 0):
                    ans = ans+"IX"
                if(i == 1):
                    ans = ans+"XC"
                if(i == 2):
                    ans = ans+ "CM"
            elif(x[b] == "4"):
                if(i == 0):
                    ans = ans+"IV"
                if(i == 1):
                    ans = ans+"XL"
                if(i == 2):
                    ans = ans+"CD"
            else:
                if(x[b] == "1"):
                    if(i == 0):
                        ans = ans+"I"
                    if(i == 1):
                        ans = ans+"X"
                    if(i == 2):
                        ans = ans+"C"
                    if(i == 3):
                        ans = ans+"M"
                if(x[b] == "2"):
                    if(i == 0):
                        ans = ans+"II"
                    if(i == 1):
                        ans = ans+"XX"
                    if(i == 2):
                        ans = ans+"CC"
                    if(i == 3):
                        ans = ans+"MM"
                if(x[b] == "3"):
                    if(i == 0):
                        ans = ans+"III"
                    if(i == 1):
                        ans = ans+"XXX"
                    if(i == 2):
                        ans = ans+"CCC"
                    if(i == 3):
                        ans = ans+"MMM"
                if(x[b] == "5"):
                    print("Test")
                    if(i == 0):
                        ans = ans+"V"
                    if(i == 1):
                        ans = ans+"L"
                    if(i == 2):
                        ans = ans+"D"
                if(x[b] == "6"):
                    if(i == 0):
                        ans = ans+"VI"
                    if(i == 1):
                        ans = ans+"LX"
                    if(i == 2):
                        ans = ans+"DC"
                if(x[b] == "7"):
                    if(i == 0):
                        ans = ans+"VII"
                    if(i == 1):
                        ans = ans+"LXX"
                    if(i == 2):
                        ans = ans+"DCC"
                if(x[b] == "8"):
                    print("test")
                    if(i == 0):
                        ans = ans+"VIII"
                    if(i == 1):
                        ans = ans+"LXXX"
                    if(i == 2):
                        ans = ans+"DCCC"
        return ans
                

                        
                
                    

                    
            
            

            
        
