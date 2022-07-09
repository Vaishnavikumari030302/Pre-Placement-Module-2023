class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        i, j = 0, n-1
        if nums[i]<nums[j]: 
            return nums[i]
        while i<j:
            mid = i+(j-i)//2
            if i+1==j:
                return nums[j]
            elif nums[mid]>=nums[i]: # go right
                i=mid
            elif nums[mid]<=nums[j]: # go left
                j=mid  