#Link to problem: https://leetcode.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        maxright = {}
        maxleft = {}
        a= []
        for i in range(len(height)):
            a.append(height[i])
        a.sort()
        for i in range(len(height)):
            j=0
            while True:
                if len(a) == 0:
                    break
                if a[0]<=height[i]:
                    maxleft[a[j]] = i
                    a.pop(0)
                else:
                    break
        for i in range(len(height)):
            a.append(height[i])
        a.sort()
        for i in range(len(height)-1, -1, -1):
            j=len(a)
            while True:
                if len(a) == 0:
                    break
                if a[0]<=height[i]:
                    maxright[a[0]] = i
            
                    a.pop(0)
                else:
                    break
        for i in range(len(height)):
            a.append(height[i])
        a.sort()
        maxwater = 0
        for i in range(len(a)):
            if((maxright[a[i]] - maxleft[a[i]])*a[i] > maxwater):
                maxwater = (maxright[a[i]] - maxleft[a[i]])*a[i]
        return maxwater
            
            
        
