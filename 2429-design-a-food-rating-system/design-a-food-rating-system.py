from sortedcontainers import SortedList
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        '''
        idea:
        sorteddict for each cuisine, key=rating, value=list
        '''
        self.ratings = defaultdict(int)
        self.cuisine = defaultdict(str)
        self.cuisines = defaultdict(SortedList)
        

        for i in range(len(foods)):
            f = foods[i]
            c = cuisines[i]
            r = ratings[i]
            self.cuisine[f] = c
            self.ratings[f] = r
            self.cuisines[c].add((r, f))



    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisine[food]
        r = self.ratings[food]
        f = food

        self.cuisines[c].remove((r, f))

        self.ratings[food] = newRating


 
        self.cuisines[c].add((newRating, f))

        

    def highestRated(self, cuisine: str) -> str:
        arr = self.cuisines[cuisine]

        for i in range(len(arr) - 2, -1, -1):
            if arr[i][0] != arr[i + 1][0]:
                return arr[i + 1][1]


        return arr[0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)