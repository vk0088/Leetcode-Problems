class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)

        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1
        count = 0
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 1 and rows[row] == 1 and cols[col] == 1:
                    count+=1
        return count
                    