class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(True):
            if(n == 0):
                break
            if(n % 2 == 1):
                count += 1
            n = int(n/2)
        return count
            
