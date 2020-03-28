class Solution:
    def minSteps(self, n: int) -> int:
        a = []
        for i in range(n+1):
            a.append(-1)
        def amin(count, sofar, copied):
            if(sofar>n):
                return 1002
            if(sofar == n):
                return count;
            return (min(amin(count+1, sofar+copied, copied), amin(count+2, sofar*2, sofar)))
        if(n == 1):
            return 0
        return amin(1, 1, 1)
