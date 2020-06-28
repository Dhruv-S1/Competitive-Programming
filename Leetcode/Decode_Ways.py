class Solution:
    def numDecodings(self, s: str) -> int:
        if(s[0] == '0'):
            return 0
        
        prev = s[0]
        newStr = prev
        for i in range(1, len(s)):
            if(s[i] == '0' and prev == '0'):
                return 0
            if(s[i] == '0' and int(prev+s[i]) >= 30):
                return 0
            if(s[i] == '0'):
                newStr = newStr[0:len(newStr)-1]
            else:
                newStr = newStr + s[i]
            prev = s[i]
        print(newStr)
        if(len(newStr) == 0 or len(newStr) == 1):
            return 1
        
        prev = newStr[0]
        dp = []
        for i in range(len(newStr)):
            dp.append(0)
        dp[0] = 1
        for i in range(1, len(newStr)):
            if(int(prev + newStr[i]) <= 26):
                if(i == 1):
                    dp[i] = 2
                else:
                    dp[i] += dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
            prev = newStr[i]
        print(dp)
        return dp[len(newStr)-1]
            
            
            
                
        
