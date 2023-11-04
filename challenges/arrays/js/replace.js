function replaceElements(arr) {
    maxsofar = -1;
    for (let i = arr.length - 1; i >= 0; i--) {
        temp = maxsofar;
        maxsofar = Math.max(maxsofar, arr[i]);
        arr[i] = temp;
    }
    return arr;
}
function reverseElements(arr) {
    // reverse elements in place
    for (let i = 0; i < arr.length / 2; i++) {
        temp = arr[i];
        arr[i] = arr[arr.length - 1 - i];
        arr[arr.length - 1 - i] = temp
    }
    return arr;
}
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(reverseElements(arr));