class Solution:
    def numTrees(self, n: int) -> int:
        a = []
        for i in range(n+1):
            a.append(-1)
        def binarytrees(n):
            if(a[n]!=-1):
                return a[n]
            if (n==0):
                return 1
            if(n == 1):
                return 1
            ans = 0
            for i in range(n):
                ans += binarytrees(i)*binarytrees(n-i-1)
            a[n] = ans
            return ans 
        return binarytrees(n)
