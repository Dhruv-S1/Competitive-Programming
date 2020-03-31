class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        d = {}
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        print(nums)
        print(d)
        count = 0
        for i in range(len(nums)):
            if((k + nums[i]) in d):
                if(k == 0):
                    count -=1
                count += d[k + nums[i]]
            if(nums[i] == k):
                count += 1
            d[nums[i]] -=1
            
        return count
                
        
