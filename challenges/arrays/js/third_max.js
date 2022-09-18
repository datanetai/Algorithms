// Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

var thirdMax = function(nums) {
    if (nums.length < 3) {
        return max_of_array(nums)
    }
    let max = max_of_array(nums);
    let max2 = max_of_array(nums.filter(x => x < max));
    let max3 = max_of_array(nums.filter(x => x < max2));
    console.log(max, max2, max3)
    return max3 ?? max
};
function max_of_array(num_array) {
    let maxsofar = num_array[0]
    for(let i = 1; i < num_array.length; i++){
        if(num_array[i] > maxsofar){
        maxsofar = num_array[i]
        }
    }
    return maxsofar
}
// test
console.log(thirdMax([1,1,2])); // 2