/**
 * @param {string} s
 * @return {boolean}
 
1. Stack to push left brackets
2. If the current character is a right bracket we would check if the last element in the stack is the matching pair. If it is then pop the left bracket off the stack, if not return false
 */
var isValid = function(s) {
    let stack = [] // Keep track of the left brackets
    let obj = {
        '(': ')',
        '{': '}',
        '[': ']'
    }; // Key value pairs to match if the right bracket matches to the top of the stack
    
    for(let char of s){ // Iterate through the string
        if(obj[char]){ // If the character is in the object then it is a left bracket and then push to stack
            stack.push(char);
        } else { // Else it is a right bracket and then check if the last element in the stack is a matching pair
            let lastElement = stack.pop(); // Last element in stack
            if(obj[lastElement] !== char){  // If the current character doesnt match the last element in the stack then it is not a pair and return false
                return false;
            }
        }
    }
    
    return true; // Return true if it passes all the checks
};
