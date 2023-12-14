class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowSums, colSums = list(map(sum, grid)), list(map(sum, zip(*grid)))
        row, col = len(colSums), len(rowSums)
        for _ in range(row*col):
            r, c = _//row, _%row
            grid[r][c] = rowSums[r]*2 + colSums[c]*2 - row - col
        return grid