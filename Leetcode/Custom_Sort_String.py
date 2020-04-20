class Solution:
    def customSortString(self, S: str, T: str) -> str:
        encode = {}
        decode = {}
        for i in range(len(S)):
            if(S[i] not in encode):
                encode[S[i]] = len(encode) + 1
                decode[encode[S[i]]] = S[i]
                
        temp_arr = []
        ans = ""
        for i in range(len(T)):
            if(T[i] in encode):
                temp_arr.append(encode[T[i]])
            else:
                ans = ans + T[i]
        temp_arr.sort()
        for i in range(len(temp_arr)):
            ans = ans + decode[temp_arr[i]]
        return ans
