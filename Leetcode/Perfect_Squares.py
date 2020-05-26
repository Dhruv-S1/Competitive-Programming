class Solution:
    def numSquares(self, n: int) -> int:
        a = []
        for i in range(n+1):
            a.append(999999999)
        a[1] = 1
        for i in range(1, n+1):
            for j in range(n):
                if(j*j > i):
                    break
                if(j*j == i):
                    a[i] = 1
                    break
                a[i] = min(a[i], a[i - j*j] + 1)
        return a[n]
