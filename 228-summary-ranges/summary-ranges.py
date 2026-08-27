class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        start=0
        for i in range(1,len(nums)+1):
            if i==len(nums) or nums[i]!=nums[i-1]+1:
                if start==i-1:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start])+"->"+str(nums[i-1]))
                start=i
        return res