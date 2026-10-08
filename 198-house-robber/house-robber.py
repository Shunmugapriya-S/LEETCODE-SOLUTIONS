class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1,rob2=0,0
        for n in nums:
            ######(rob1,rob2,n,n+1)here rob1+n is taken rob2 is neglected ..detemine the max amount that can be robbed from the home 
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
