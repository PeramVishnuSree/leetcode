# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone,
# return the largest possible number of stones that can be removed.

# insights
# 1. In a connected component, we can always remove all stones except one
# 2. Moves in one component do not affect other components.
# 3. Each stone belongs to exactly one component
