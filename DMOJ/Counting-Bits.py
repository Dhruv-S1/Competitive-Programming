class Solution:
    def countBits(self, num: int) -> List[int]:
        a = [0, 1, 1]
        if(num == 0):
            return [0]
        if(num == 1):
            return [0, 1]
        if(num == 2):
            return a
        greatest = 2
        for i in range(3, num+1):
            if(greatest*2 == i):
                greatest = i
                a.append(1)
                continue
            a.append(a[greatest] + a[i - greatest])
        return a
        
