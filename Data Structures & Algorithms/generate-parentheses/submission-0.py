class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def build(current, open_count, close_count) -> None:
            if open_count == n and close_count == n:
                res.append(current)
                return
            if open_count < n:
                build(current + "(", open_count + 1, close_count)
            if open_count > close_count:
                build(current + ")", open_count, close_count + 1)
        
        build("", 0, 0)
        return res


            
            