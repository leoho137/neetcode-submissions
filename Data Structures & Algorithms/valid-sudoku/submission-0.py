class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  
        # check rows -- O(n^2)
        for i in range(9):
            check = set()
            for j in range(9):
                x = board[i][j]
                if x == ".":
                    continue
                if x not in check:
                    check.add(x)
                else:
                    return False
        # check columns -- O(n^2)
        for j in range(9):
            check = set()
            for i in range(9):
                x = board[i][j]
                if x == ".":
                    continue
                if x not in check:
                    check.add(x)
                else:
                    return False
        # check 3x3 grids --
        offset_1 = 0
        offset_2 = 0
        for offset_1 in range(3):
            for offset_2 in range(3):
                check = set()
                for k in range(3 * offset_1, 3 + 3 * offset_1):
                    for l in range(3 * offset_2, 3 + 3 * offset_2):
                        x = board[k][l]
                        if x == ".":
                            continue
                        if x not in check:
                            check.add(x)
                        else:
                            return False
        return True
