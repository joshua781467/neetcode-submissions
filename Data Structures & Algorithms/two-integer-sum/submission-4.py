class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maping = {}
        for i , num in enumerate(nums):
            maping[num] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in maping:
                if i != maping[diff]:
                    return [i,maping[diff]]

        