# Find the longest substring in the given string without repeating the characters.
# Sliding window method is used to further optimise the code
    def lengthOfLongestSubstring(self, s) :

        i = 0
        d = {}
        ans = 0
        for j in range(len(s)):
            if s[j] in d:
                i = max(i,d[s[j]])
            ans = max(ans,j-i+1)
            d[s[j]] = j+1

        return ans