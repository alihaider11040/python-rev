class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        if (len(s) == len(set(s))):
            return len(s)
        currentSize = len(s)
        end = currentSize - 1
        start = 1
        while(currentSize != 1):
            while (start > 0 ):
                if ((maxlen < len(s[start:end])) and (len(s[start:end]) == len(set(s[start:end])))):
                    maxlen = len(s[start:end])
                start = start -1
                end   = end - 1
            currentSize = currentSize -1
            end = len(s) - 1
            start = len(s) - currentSize
        if (maxlen > 1):
            return maxlen
        else:
            return 1


            
        