class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left=sum(cardPoints[:k])
        right=0
        maxsum=left
        n=len(cardPoints)
        for i in range(1,k+1):
            left-=cardPoints[k-i]
            right+=cardPoints[n-i]
            maxsum=max(maxsum,right+left)
        return maxsum