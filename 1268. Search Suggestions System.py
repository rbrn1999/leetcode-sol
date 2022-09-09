# link: https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        for i in range(len(searchWord)):
            # could use binary search to optimize
            products = [product for product in products if len(product) > i and product[i] == searchWord[i]]
            res.append(products[:3])
        return res