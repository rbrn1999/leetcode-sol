# link: https://leetcode.com/problems/design-a-food-rating-system/

from collections import defaultdict
from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cusine = {foods[i]: cuisines[i] for i in range(len(foods))}
        self.food_rating = {foods[i]: ratings[i] for i in range(len(foods))}
        self.cuisine_foods = defaultdict(lambda: SortedList(key=lambda x: (-x[1], x[0])))
        for i in range(len(foods)):
            self.cuisine_foods[cuisines[i]].add((foods[i], ratings[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cusine[food]
        rating = self.food_rating[food]
        self.cuisine_foods[cuisine].discard((food, rating))
        self.cuisine_foods[cuisine].add((food, newRating))
        self.food_rating[food] = newRating
    
    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_foods[cuisine][0][0]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)