class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            for j in range(9):
                entry = board[i][j]
                if not entry.isalnum():
                    continue
                if entry in row_set:
                    return False
                else:
                    row_set.add(entry)
            
        for j in range(9):
            column_set = set()
            for i in range(9):
                entry = board[i][j]
                if not entry.isalnum():
                    continue
                if entry in column_set:
                    return False
                else:
                    column_set.add(entry)


        for up_i in range(3):
            for up_j in range(3):
                box_set = set()
                for i in range(up_i * 3, up_i * 3 + 3):
                    for j in range(up_j * 3, up_j * 3 + 3):
                        entry = board[i][j]
                        if not entry.isalnum():
                            continue
                        if entry in box_set:
                            return False
                        else:
                            box_set.add(entry)
        return True
