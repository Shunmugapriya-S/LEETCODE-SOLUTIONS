class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for i,num1 in count.items():
            if num1==1:
                return i

            
        