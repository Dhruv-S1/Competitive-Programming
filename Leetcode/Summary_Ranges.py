class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(len(nums) == 0):
            return nums
        start = nums[0]
        end = nums[0]
        ans = []
        marker = 1
        for i in range(1, len(nums)):
            if(nums[i] == end + 1):
                end = nums[i]
            else:
                if(start != end):
                    ans.append(str(start) + "->" + str(end))
                else:
                    ans.append(str(start))
                start = nums[i]
                end = nums[i]
        if(start != end):
            ans.append(str(start) + "->" + str(end))
        else:
            ans.append(str(start))
        return ans
                
            
            
            
        
