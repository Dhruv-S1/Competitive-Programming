class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def custom(num1, num2):
            str1 = str(num1)
            str2 = str(num2)
            print(str1)
            if(int(str1+str2) > int(str2+str1)):
                return True
            else:
                return False
                
        def merge(arr1, arr2):
            pointer1 = 0
            pointer2 = 0
            temp = []
            
            while(True):
                if(pointer1 == len(arr1) or pointer2 == len(arr2)):
                    break
                if(custom(arr1[pointer1], arr2[pointer2])):
        
                    temp.append(arr1[pointer1])
                    pointer1 += 1
                else:
                    temp.append(arr2[pointer2])
                    pointer2 += 1
            if(pointer1 < len(arr1)):
                for i in range(pointer1, len(arr1)):
                    temp.append(arr1[i])
            if(pointer2 < len(arr2)):
                for i in range(pointer2, len(arr2)):
                    temp.append(arr2[i])
            return temp       
                    
        def mergeSort(arr):
            if(len(arr) == 1):
                return arr
            left = []
            right = []
            for i in range(int(len(arr)/2)):
                left.append(arr[i])
            for i in range(int(len(arr)/2), len(arr)):
                right.append(arr[i])
            ans1 = mergeSort(left)
            ans2 = mergeSort(right)
            return merge(ans1, ans2)
        ans = mergeSort(nums)
        ansStr = ''
        for i in range(len(ans)):
            ansStr = ansStr + str(ans[i])
        if(ansStr[0] == '0'):
            return '0'
        else:
            return ansStr
            
