class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last position of each character
        char_index_map = {}
        max_len = 0
        start = 0  # The starting index of the window
        
        # Traverse the string with the `end` pointer
        for end in range(len(s)):
            # If the character is already in the window, move the start pointer
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1
            
            # Update the last seen index of the character
            char_index_map[s[end]] = end
            
            # Calculate the length of the current window and update `max_len`
            max_len = max(max_len, end - start + 1)
        
        return max_len
