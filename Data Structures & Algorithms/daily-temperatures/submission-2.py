class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_stack = []
        l = len(temperatures)
        res = [0] * l
        for i in range(l):
            while t_stack and t_stack[-1][1] < temperatures[i]:
                t = t_stack.pop()
                res[t[0]] = i - t[0]
            if i != l - 1 and temperatures[i] < temperatures[i + 1]:
                res[i] = 1
            else:
                res[i] = 0
                t_stack.append((i, temperatures[i]))       
        return res
            