class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_num = -1
            for j in range(i+1,len(arr)):
                max_num= max(arr[j],max_num)
            arr[i] = max_num
    
        return arr



        