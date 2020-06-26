class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = {}
        b = {}
        for i in range(len(nums1)):
            if(nums1[i] in a):
                a[nums1[i]] += 1
            else:
                a[nums1[i]] = 1
        for i in range(len(nums2)):
            if(nums2[i] in b):
                b[nums2[i]] += 1
            else:
                b[nums2[i]] = 1
        ans = []
        for key in b:
            if(key in a):
                for i in range(min(b[key], a[key])):
                    ans.append(key)
        return ans
                
