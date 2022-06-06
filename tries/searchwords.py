# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed.
# Suggested products should have common prefix with searchWord.
# If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of arrays of the suggested products after each character of searchWord is typed.




class Solution:
    def suggestedProducts(self, products, searchWord):

        ans = []
        for i in range(1, len(searchWord) + 1):
            arr = []
            for word in products:
                if word.startswith(searchWord[:i]) is True:
                    arr.append(word)

            arr.sort()
            if len(arr) >= 3:
                ans.append(arr[:3])
            else:
                ans.append(arr)

        return ans