function binary_search(nums, target) {
    let left = 0; // [0* , 1, 2, 3, 4, 5, 6, 7, 8, 9]
    let right = arr.length - 1; // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9*]
    while (left <= right) {
        // use mid = l+(r-l)/2 to avoid overflow
        let mid = Math.floor(left + (right - left) / 2);
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
/* array of length 1
left = 0
right = 0
mid = 0
update left = mid + 1 = 1
left > right
array of length 2
left = 0
right = 1
mid = 0
update left = mid + 1 = 1
left = right
array of length 3
left = 0
right = 2
mid = 1
update right = mid - 1 = 0
left > right

*/
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
target = 6;
console.log(binary_search(arr, target));
