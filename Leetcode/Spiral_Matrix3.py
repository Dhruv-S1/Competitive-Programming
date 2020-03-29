class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        import math
        face = 0 # 0 - E, 1 - S, 2 - W, 3 - N
        count = 0
        count1 = 0
        ans = []
        while(True):

            count1 += 1
            if(count >= (R)*(C)):
                break
            if(face == 0):
                for i in range(c0, c0 +math.ceil((count1/2))):
                    if((r0 < R) and (i< C) and (r0 >=  0) and (i>= 0)):
                        count += 1
                        ans.append([r0, i])
                c0 += math.ceil((count1/2))
                face = 1
                continue
                    
            if(face == 1):
                for i in range(r0, r0 +math.ceil((count1/2))):
                    if((i  < R) and (c0 < C) and (i >=  0) and (c0 >= 0)):
                        count += 1
                        ans.append([i, c0])
                r0 += math.ceil((count1/2))
                face = 2
                continue
                    
            if(face == 2):
                for i in range(c0, c0 - math.ceil((count1/2)), -1):
                    if((r0 < R) and (i < C) and (r0 >=  0) and (i>= 0)):
                        count += 1
                        ans.append([r0, i])
                c0 -= math.ceil((count1/2))
                face = 3
                continue
            if(face == 3):
                for i in range(r0, r0 - math.ceil((count1/2)), -1):
                    if((i < R) and (c0 < C) and (i >=  0) and (c0 >= 0)):
                        count += 1
                        ans.append([i, c0])
                r0 -= math.ceil((count1/2))
                face = 0
                continue
        return ans

                
            
