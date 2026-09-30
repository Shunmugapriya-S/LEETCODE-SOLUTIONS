class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        pq=[]
        for i in stones:
            heapq.heappush(pq,-i)
        while len(pq)>1:
            y=-heapq.heappop(pq)
            x=-heapq.heappop(pq)
            if y!=x:
                heapq.heappush(pq,-(y-x))
        if pq:
            return -pq[0]
        return 0 