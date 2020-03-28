class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        d = {}
        d[A[0]] = 1
        b = []
        for i in range(len(A)):
            if(A[i] != 0):
                b.append(1)
            else:
                b.append(0)
        for i in range(1, len(A)):
            A[i] = A[i] + A[i-1]
            if (A[i] in d):
                d[A[i]] += 1
            else:
                d[A[i]] = 1
        answer = 0
        print(A)
        for i in range(len(A)):
            if((A[i] + S) in d):
                if(d[(A[i] + S)] != 0):
                    if(S == 0):
                        if(b[i] == 0):
                            answer += d[(A[i] + S)]
                    else:
                        answer += d[(A[i] + S)]
            if(A[i] == S and S != 0):
                answer += 1
            d[A[i]] -= 1
            
        return answer
        
            
