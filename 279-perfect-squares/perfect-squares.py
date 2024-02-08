class Solution:
    def numSquares(self, n: int) -> int:
        def dfs(total):
            nonlocal sqrtNum

            # base 1; infeasible
            if total > n:
                return float('inf')

            # base 2; feasible
            if total == n:
                return 0

            # seen before
            if total in memo:
                return memo[total]

            # otherwise calculate memo[total]
            res = float('inf')

            # iterate over possible valid square values
            for num in sqrtNum:
                # stop searching sqrtNum
                if total + num > n:
                    break

                # add num and recur
                temp = 1 + dfs(total + num)

                # compare
                res = min(res, temp)

            memo[total] = res

            return memo[total]

        # list of valid perfect numbers
        sqrtNum = [num ** 2 for num in range(1, int(n ** 0.5) + 1)]

        # meme[total] := minimum number of perfect square numbers that sum to total
        memo = dict()

        return dfs(0)