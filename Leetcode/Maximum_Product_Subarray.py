class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        imin = ans
        imax = ans
        for i in range(1, len(nums)):
            print(ans, imax, imin)
            if(nums[i] < 0):
                temp = imax
                imax = max(nums[i], imin*nums[i])
                imin = min(nums[i], temp*nums[i])
            elif(nums[i] > 0):
                imax = max(nums[i], imax*nums[i])
                imin = min(nums[i], imin*nums[i])
            else:
                imax = 0
                imin = 0
            ans = max(ans, imax)
        return ans
