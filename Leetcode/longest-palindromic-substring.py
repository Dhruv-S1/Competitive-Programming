# Link to leetcode problem: https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        a = []
        b = []
        if(s == s[::-1]):
            return s
        for j in range(len(s)):
            b = []
            for k in range(len(s)):
                b.append(0)
            a.append(b)
        for i in range(len(s)):
            a[i][i] = 1
        maxcount= 0
        beg = 0
        end = 0
        for i in range(1, len(s)):
            if(s[i] == s[i-1]):
                a[i-1][i] = 1
                maxcount = 2
                beg = i-1
                end = i+1
        for i in range(len(s)-2, -1, -1):
            for j in range(len(s)-1, i-1, -1):
                if(a[i+1][j-1] and s[i] == s[j]):
                    a[i][j] = 1
        
        for i in range(len(s)):
            for j in range(len(s)):
                if(a[i][j] and j-i+1>maxcount):
                    maxcount = j-i+1
                    beg = i
                    end = j+1
        return s[beg:end]
        
