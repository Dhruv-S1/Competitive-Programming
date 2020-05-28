class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = {}
        S = {}
        count = 0
        for i in range(len(t)):
            S[t[i]] = 0
            if(t[i] in T):
                T[t[i]] += 1
            else:
                T[t[i]] = 1
        start = 0
        end = 0
        minString = ""
        minLength = 999999999
        if(s[0] in T):
            S[s[0]] += 1
            if(S[s[0]] >= T[s[0]]):
                count += 1
        while(True):
            if(count == len(T)):
                if(end - start + 1 < minLength):
                    minLength = end - start + 1
                    minString = s[start:end+1]
                if(s[start] in T):
                    S[s[start]] -= 1
                    if(S[s[start]]+1 >= T[s[start]] and S[s[start]] < T[s[start]]):
                        count -= 1
                start += 1
            elif(end == len(s) - 1):
                break
            else:
                end += 1
                if(s[end] in T):
                    S[s[end]] += 1
                    if(S[s[end]]-1 < T[s[end]] and S[s[end]] >= T[s[end]]):
                        count += 1
        return minString
                
                
            
                
            
            
        
