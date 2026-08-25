class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()#REMOVE TRAILING AND WHITE SPACES 
        word=s.split()#SPLIT THE WORD SUCH AS SKY IS BLUE
        reversed_words=word[::-1]#REVERSE THE WORD 
        return " ".join(reversed_words)# "" -refers to the space betweem the words 
        