class Solution:
    def maxSubArray(self,nums:list[int])->int:
        maxsum=nums[0]
        currsum=0
        for n in nums:
            if currsum<0:
                currsum=0
            currsum+=n
            maxsum=max(currsum,maxsum)
        return maxsum


        