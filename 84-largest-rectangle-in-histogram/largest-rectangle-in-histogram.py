class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        pse=[-1]*n
        nse=[0]*n
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]] >=heights[i]:
                stack.pop()
            pse[i]=stack[-1] if stack else -1
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            nse[i]=stack[-1] if stack else n
            stack.append(i)
        max_area=0
        for i in range(n):
            w=nse[i]-pse[i]-1
            area=heights[i]*w
            max_area=max(area,max_area)
        return max_area