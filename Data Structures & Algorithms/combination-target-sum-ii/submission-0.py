class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        candidates.sort()
        def backtracking(i: int, total: int):
            if total == target:
                res.append(arr.copy())
                return
            if total < target:
                for j in range(i, len(candidates)):
                    if j > i and candidates[j] == candidates[j - 1]:
                        continue
                    arr.append(candidates[j])
                    backtracking(j + 1, total + candidates[j])
                    arr.pop()            

        backtracking(0, 0)
        return res
            