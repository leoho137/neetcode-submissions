class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        res = 0
        dq = deque()
        for x in tokens:
            if x in operators:
                # operate
                operator = x
                b = int(dq.pop())
                a = int(dq.pop())
                match operator:
                    case '+':
                        res = a + b
                    case '-':
                        res = a - b
                    case '*':
                        res = a * b
                    case '/':
                        res = a // b
                        if res < 0 and a % b != 0:
                            res += 1
                dq.append(res)
            else:
                dq.append(x)
        return int(dq.pop())