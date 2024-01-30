class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        def is_operator(s):
            return s in ["+", "-", "*", "/"]

        for token in tokens:
            if is_operator(token):
                ele2 = int(st.pop())
                ele1 = int(st.pop())
                if token == "+":
                    result = ele1 + ele2
                elif token == "-":
                    result = ele1 - ele2
                elif token == "/":
                    result = int(ele1 / ele2)
                elif token == "*":
                    result = ele1 * ele2
                st.append(str(result))
            else:
                st.append(token)
        return int(st[-1])