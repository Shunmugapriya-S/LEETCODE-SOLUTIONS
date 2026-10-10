class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        res=[]
        for ch in s:
            if ch=="(":
                if stack:
                    res.append(ch)
                stack.append(ch)
            else:
                stack.pop()
                if stack:
                    res.append(ch)
        return "".join(res)