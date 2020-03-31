class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        ans = []
        for i in range(len(queries)):
            if(queries[i][0] == 0):
                ans.append(arr[queries[i][1]])
                continue
            ans.append(arr[queries[i][1]]^arr[queries[i][0]-1])
        return ans
            
