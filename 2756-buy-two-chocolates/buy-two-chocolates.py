class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sort_arr = sorted(prices)
        if (money - sum(sort_arr[0:2])) <0:
            return money 
        else :
            return (money - sum(sort_arr[0:2]))