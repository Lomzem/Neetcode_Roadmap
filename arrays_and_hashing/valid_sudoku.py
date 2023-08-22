import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # rows = [(5, 3, 7), (6, 1, 9, 5)]
        # cols = [(5, 6)]
        # squares = {(0, 0): (5, 3, 7)}

        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = collections.defaultdict(list)

        for row in range(9):
            for cell in range(9):
                if board[row][cell] == '.':
                    continue

                cell_value = board[row][cell]
                if (cell_value in rows[row] or
                    cell_value in cols[cell] or
                    cell_value in squares[(row // 3, cell // 3)]):
                    return False

                rows[row].append(cell_value)
                cols[cell].append(cell_value)
                squares[(row // 3, cell // 3)].append(cell_value)

        return True
