class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        def flip(index):
            for i in range(int((index+1)/2)):
                temp = A[i]
                A[i] = A[index - i]
                A[index - i] = temp
                
        for i in range(len(A), 0, -1):
            for j in range(len(A)):
                if(A[j] == i and j+1 == i):
                    break
                elif (A[j] == i):
                    flip(j)
                    ans.append(j+1)
                    flip(i-1)
                    ans.append(i)
                    break
        return ans
                

        
