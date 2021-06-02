
// Loop through the array, for each number I will subtract the target from the number
// Store the result in a object with the index of the array
// Check if the current number is in the object, if so then return, else then add the value of the target subtracted by the number
var twoSum = function(nums, target) {
    let obj = {};
    for(let i = 0; i < nums.length; i++){    
       if(obj[nums[i]] >= 0) {
           return [obj[nums[i]], i];
       }
        
        let result = target - nums[i];
        obj[result] = i;              
    }
};
