class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        q=deque(range(len(deck)))
        answer=[0]*len(deck)
        for card in deck:
            position=q.popleft()
            answer[position]=card
            if q:
                next=q.popleft()
                q.append(next)
        return answer


        