class Solution:
    def canJump(self, nums: List[int]) -> bool:
        highest = 0
        for i in range(len(nums)):
            if(nums[i] == 0):
                if(i == len(nums)-1):
                    return True
                if(highest == i):
                    return False
                else:
                    continue
            highest = max(highest, i + nums[i])
        return True
        
