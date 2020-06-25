class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if(len(strs) == 0):
            return ''
        for i in range(len(strs[0])):
            prefix = strs[0][0:i+1]
            for j in range(len(strs)):
                if(len(strs[j]) >= len(prefix) and strs[j][0:i+1] == prefix):
                    continue
                else:
                    return strs[0][0:i]
        return prefix
           
            
                
        
