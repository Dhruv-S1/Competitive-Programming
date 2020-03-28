class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        x = 2**len(nums)
        binary = []
        temp = 0
        visited = set()
        for i in range(1, x):
            binary.append(bin(i)[2:].zfill(len(nums)))
        for i in range(len(binary)):
            a = []
            for j in range(len(binary[i])):
                if(binary[i][j] == '1'):
                    a.append(nums[j])
            a.sort()
            if (tuple(a) not in a):
                visited.add(tuple(a))
        ans = []
        for key in visited:
            a = []
            for i in range(len(key)):
                a.append(key[i])
            ans.append(a)

        ans.append([])
        return ans
                
