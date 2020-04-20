class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(len(nums)):
            nums[nums[i]%n] += n
        for i in range(len(nums)):
            if(nums[i] - 2*n > 0 and nums[i] - 2*n <= n):
                if(i == 0):
                    ans.append(len(nums))
                else:
                    ans.append(i)
        return ans
