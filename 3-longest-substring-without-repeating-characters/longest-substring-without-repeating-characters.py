class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Given a string s, find the length of the longest substring without duplicating characters.
        # A substring is a contiguous non-empty sequence of characters within a string
        ans = 0 # ans - length of the longest substring
        hashSet = set()
        curr = 0
        begin = 0
        if len(s) == 0:
            return 0
        for chr in s: # loop through s
            if chr in hashSet:
                while chr !=  s[begin]:
                    hashSet.remove(s[begin])
                    begin += 1
                begin += 1
                # [1,2,3, 4,3,5,6,7,8,9,10,11,12,13]
            else:
                hashSet.add(chr)
            if curr - begin > ans:
                ans = curr - begin
            curr += 1
        return ans + 1