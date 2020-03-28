class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = {}
        a[nums[0]] = 0
        for i in range(1, len(nums)):
            if((target-nums[i]) in a):
              return [a[target-nums[i]], i]
            else:
              a[nums[i]] = i
                
