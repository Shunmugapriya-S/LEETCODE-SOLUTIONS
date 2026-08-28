class Solution:
    def isValid(self,s:str)->bool:
        stack=[]
        stackops={
            "(":")",
             "[":"]",
             "{":"}",
        }
        for ch in s:
            if ch in stackops:
                stack.append(ch)
            else:
                if stack and stackops[stack[-1]]==ch:
                    stack.pop()
                else:
                    return False
        return True if not stack else False


