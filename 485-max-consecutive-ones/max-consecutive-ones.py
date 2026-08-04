class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_count=0
        for i in nums:
            if i==1:
                count+=1
                max_count=max(max_count,count)
            else:
                count=0 
        return max_count
        ##max_count=max(max_count,count)-if defined outside the loop it would count the values after the loop is finished so that would not efficient 
            