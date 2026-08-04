# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         n=len(nums)
#         k%=n
#         def rev(left,right):
#             while left<right:
#                 nums[left],nums[right]=nums[right],nums[left]
#                 left+=1
#                 right-=1
#         rev(0,n-1)
#         rev(0,k-1)
#         rev(k,n-1)
class Solution:
    def rotate(self,nums:list[int],k:int):
        n=len(nums)
        k%=n
        ans=[0]*n
        for i in range(n):
            ans[(i+k)%n]=nums[i]
        nums[:]=ans