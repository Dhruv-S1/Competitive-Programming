class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        pointerA = 0
        pointerB = 0
        ans = []
        while(True):
            if(pointerA == len(A)):
                break
            if(pointerB == len(B)):
                break
            if(A[pointerA][0] <= B[pointerB][0] and A[pointerA][1] >= B[pointerB][0]):
                if(B[pointerB][1] < A[pointerA][1]):
                    ans.append([B[pointerB][0], B[pointerB][1]])
                else:
                    ans.append([B[pointerB][0], A[pointerA][1]])
            elif(A[pointerA][0] >= B[pointerB][0] and A[pointerA][0] <= B[pointerB][1]):
                if(B[pointerB][1] > A[pointerA][1]):
                    ans.append([A[pointerA][0], A[pointerA][1]])
                else:
                    ans.append([A[pointerA][0], B[pointerB][1]])
            if(A[pointerA][1] > B[pointerB][1]):
                pointerB += 1
            elif(A[pointerA][1] < B[pointerB][1]):
                pointerA += 1
            else:
                pointerA += 1
                pointerB += 1
        return ans
