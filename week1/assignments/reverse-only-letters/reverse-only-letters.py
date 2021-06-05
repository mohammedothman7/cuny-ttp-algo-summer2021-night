class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Reverse string with two pointers one at the beginning of the string and one at the end.
        # Left pointer will scan for special characters and the right pointer will scan for letters
        # If both the left and right character at each index are letters than add the right character to the string and increment the left pointer and decrement the right pointer
        # If the left is not a letter and the right is then add the special character to the string and only increment the left pointer
        # If both pointers are special characters then only decrement the right pointer because the left pointer is the one to scan for special characters
        
        
        left = 0 #Left Pointer
        right = len(s) - 1 #Right pointer
        rev_str = "" #Reversed string
        
        if(len(s) == 1): return s
        
        while left < len(s):
            if s[left].isalpha() and s[right].isalpha(): #Example: asada
                rev_str += s[right]
                left += 1
                right -= 1
            elif not s[left].isalpha(): #Example: !asada
                rev_str += s[left]
                left += 1
            else: #Example: !adsada!
                right -= 1
                
        return rev_str
                
        
