class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.sumofsquares(n)
            if n==1:
                return True
        return False
    def sumofsquares(self,n:int):
        out=0
        while n:
            digit=n%10
            digit=digit**2
            out+=digit
            n//=10
        return out 