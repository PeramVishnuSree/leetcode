# You are given an integer array height of length n. T
# here are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        area = 0
        while j > i:
            ar = min(height[i], height[j]) * (j - i)
            if ar > area:
                area = ar
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1

        return area