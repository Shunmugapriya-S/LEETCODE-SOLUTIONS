class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_area=0
        while l<=r:
            wid=r-l
            length=min(height[l],height[r])
            area=length*wid
            max_area=max(max_area,area)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return max_area