# link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

# DFS
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        def canMake(recipe: str, making = set()) -> bool:
            if recipe in canMake_cache:
                return canMake_cache[recipe]

            # cycle detected
            if recipe in making:
                return False
            making.add(recipe)


            for ingredient in recipe_ingredients[recipe]:
                if ingredient in supplie_set:
                    pass
                elif ingredient in recipe_ingredients:
                    if not canMake(ingredient, making):
                        canMake_cache[recipe] = False
                        return False
                else:
                    canMake_cache[recipe] = False
                    return False

            making.remove(recipe)
            canMake_cache[recipe] = True
            return True


        result = []
        canMake_cache = {}
        recipe_ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        supplie_set = set(supplies)
        for recipe in recipes:
            if canMake(recipe):
                result.append(recipe)

        return result

# Topological Sort (Kahn's algorithm)

from collections import deque, defaultdict
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        supplie_set = set(supplies)
        recipe_set = set(recipes)
        ingredient_recipe = defaultdict(list)
        indegree = {}

        for i in range(len(recipes)):
            indegree[recipes[i]] = 0
            for ingredient in ingredients[i]:
                if ingredient in supplie_set:
                    continue
                if ingredient in recipe_set:
                    ingredient_recipe[ingredient].append(recipes[i])
                indegree[recipes[i]] += 1

        q = deque(recipe for recipe in recipes if indegree[recipe] == 0)

        result = []
        while q:
            recipe = q.popleft()
            result.append(recipe)

            for next_recipe in ingredient_recipe[recipe]:
                indegree[next_recipe] -= 1
                if indegree[next_recipe] == 0:
                    q.append(next_recipe)

        return result
