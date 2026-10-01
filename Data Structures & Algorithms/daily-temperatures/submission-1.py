class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_stack = []
        res = []
        for i in range(len(temperatures)):
            while t_stack and t_stack[-1][1] < temperatures[i]:
                t = t_stack.pop()
                res[t[0]] = i - t[0]
            if i != len(temperatures) - 1 and temperatures[i] < temperatures[i + 1]:
                res.append(1)
            else:
                res.append(0)
                t_stack.append((i, temperatures[i]))       
        return res
            