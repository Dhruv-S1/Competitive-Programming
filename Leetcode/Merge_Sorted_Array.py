class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans = []
        a = 0 # nums1
        b = 0 # nums2
        while(True):
            if(a == m and b == n):
                for i in range(len(nums1)):
                    nums1[i] = ans[i]
                break
            elif(a == m):
                ans.append(nums2[b])
                b += 1
            elif(b == n):
                ans.append(nums1[a])
                a += 1
            elif(nums1[a] >= nums2[b]):
                ans.append(nums2[b])
                b += 1
            else:
                ans.append(nums1[a])
                a += 1
            
