class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"]":"[","}":"{",")":"("}
        stack = []
        
        for ch in s:
            # opening bracket
            if ch not in pairs:
                stack.append(ch)

            # closed bracket
            else:
                # no opening bracket available
                if not stack:
                    return False

                # top doesnt match
                if stack[-1] != pairs[ch]:
                    return False

                # match found
                stack.pop()

        return len(stack) == 0