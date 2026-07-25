class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k=k%len(nums)
        l=0
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=l+1,r-1
        ##sort the first 
        l=0
        r=k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=l+1,r-1
        #sort the remaining 
        l,r=k,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=l+1,r-1