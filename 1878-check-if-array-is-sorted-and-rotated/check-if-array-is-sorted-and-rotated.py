class Solution:
    def check(self,nums:List[int])->bool:
        N=len(nums)
        count=1
        for i in range(1,2*N):#duplicating the same 3 4 5 1 2 3 4 5 1 2 here 1 2 3 4  5
            if nums[(i-1)%N]<=nums[i%N]:
                count+=1
            else:
                count=1
            if count>=N:
                return True
        return False