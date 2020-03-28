from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        h = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        x = 0
        for key in d:
            if(len(h)==k):
                x = heapq.nsmallest(1, h)[0][0]
                if(x<d[key]):
                    heappop(h)
                    heappush(h, (d[key], key))
            else:
                heappush(h, (d[key], key))

        a = heapq.nlargest(k, h)
        b = []
        for i in range(len(a)):
            b.append(a[i][1])
        return b
            
            
        
            
        
