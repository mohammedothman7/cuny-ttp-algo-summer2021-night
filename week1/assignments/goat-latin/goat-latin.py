class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # Have a set of the lowercase vowels
        # Split the sentence by spaces and iterate through it`
        # Check if the word starts with a vowel, if so then add "ma" to the end and also "a" times the index
        # If the word does not start with a vowel than remove the first letter of the word and append it to the end of the word and then add "ma" and "a" times the index
        # We will need a array to store all the updated words
        # Then at the end join the updated words array and seperate the words by a space
        
        
        words = [] # Store all the new updated words
        vowels = set("aeiou") # Set to check if word starts with a vowel
        
        for i in range(len(sentence.split(" "))): # Iterate through the list of words
            word = sentence.split(" ")[i] # Get the word at the index
            
            if word[0].lower() in vowels: # If the word starts with a vowel than add "ma" and "a" times the index to the end
                word += "ma" + 'a' * (i+1)
            else: # If it does not start with a vowel than remove the first letter of the word and append to the end
                word = word[1:] + word[0] + "ma" + 'a' * (i+1)
                
            words.append(word) # Add the word to the words array
            
        return " ".join(words) # Join all the updated words in the array and add a space between each word
