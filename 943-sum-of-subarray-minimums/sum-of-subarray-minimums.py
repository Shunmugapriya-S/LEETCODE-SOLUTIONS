class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        n=len(arr)
        mod=10**9+7
        l=[0]*n
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            l[i]=i-(stack[-1] if stack else -1)
            stack.append(i)
        r=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            r[i]=(stack[-1] if stack else n)-i
            stack.append(i)
        result=0
        for i in range(n):
            result+=arr[i]*l[i]*r[i]
            result%=mod
        return result