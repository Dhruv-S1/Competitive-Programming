#Link to problem: https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        p1 = 0 
        p2 = 0
        count = 1
        maxcount = 0
        if(len(s)==0):
            return 0
        if(len(s)==1):
            return 1
        a = set()
        a.add(s[p1])
        while(True):
            p2+=1
            if(p2==len(s)):
                break
            if(s[p2] in a):
                while(True):
                    if(s[p1] == s[p2]):
                        a.remove(s[p1])
                        p1+=1
                        count-=1
                        break;
                    count-=1
                    a.remove(s[p1])
                    p1+=1
            
            
            count+=1
            if(count>maxcount):
                maxcount = count
            a.add(s[p2])
        return maxcount
            
            
        
