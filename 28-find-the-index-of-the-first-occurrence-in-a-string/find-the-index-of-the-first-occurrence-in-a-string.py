class Solution:## kmp 
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        lps=[0]*len(needle)
        prevlps,i=0,1
        while i<len(needle):
            if needle[i]==needle[prevlps]:
                prevlps+=1
                lps[i]=prevlps
                i+=1
            elif prevlps==0:
                lps[i]=0
                i+=1
            else:
                prevlps=lps[prevlps-1]
        i=0
        j=0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                i,j=i+1,j+1
                if j==len(needle):
                        return i-len(needle)
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]
                    
        return -1