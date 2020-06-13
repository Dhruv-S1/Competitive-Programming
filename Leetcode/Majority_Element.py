class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boter-Moore Voting Algorithm
        count = 1
        current = nums[0]
        for i in range(1, len(nums)):
            if(count == 0):
                current = nums[i]
                count = 1
            elif(nums[i] != current):
                count -= 1
            else:
                count+=1
        return current
                
                
        
