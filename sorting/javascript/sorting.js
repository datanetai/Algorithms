class BogoSorter {
    // Making the methods static as they don't depend on the instance state.
    static isSorted(arr) {
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) return false;
        }
        return true;
    }

    static shuffle(arr) {
        let shuffled = [];
        while (arr.length > 0) {
            let index = Math.floor(Math.random() * arr.length);
            shuffled.push(arr[index]);
            arr.splice(index, 1);
        }
        return shuffled;
    }

    static bogosort(arr) {
        // Making a copy of the array to avoid side effects.
        let copyArr = [...arr];
        while (!this.isSorted(copyArr)) {
            copyArr = this.shuffle([...copyArr]);
        }
        return copyArr;
    }
}

function bubbleSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = arr.length - 1; j > i; j--) {
            if (arr[j] < arr[j - 1]) {
                let temp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = temp;
            }
        }
    }
    return arr;
}

function selectionSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let minIndex = i;
        let minValue = arr[i];
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < minValue) {
                minIndex = j;
                minValue = arr[j];
            }
        }
        let temp = arr[i];
        arr[i] = minValue;
        arr[minIndex] = temp;
    }
    return arr;
}

function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let j = i;
        let current = arr[i];
        while (j > 0 && current < arr[j - 1]) {
            arr[j] = arr[j - 1];
            j--;
        }
        arr[j] = current
    }
    return arr;
}

function merge(left_arr, right_arr) {
    let leftIndex = 0;
    let rightIndex = 0;
    let result = [];
    while (leftIndex < left_arr.length && rightIndex < right_arr.length) {
        if (left_arr[leftIndex] < right_arr[rightIndex]) {
            result.push(left_arr[leftIndex]);
            leftIndex++;
        } else {
            result.push(right_arr[rightIndex]);
            rightIndex++;
        }
    }
    return result.concat(left_arr.slice(leftIndex)).concat(right_arr.slice(rightIndex));
}

function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    let middle = Math.floor(arr.length / 2);
    let left_arr = arr.slice(0, middle);
    let right_arr = arr.slice(middle);
    return merge(mergeSort(left_arr), mergeSort(right_arr));
}

function merge2(A, p, q, r) {
    // Compute the lengths of the two subarrays
    let n1 = q - p + 1;
    let n2 = r - q;

    // Initialize temporary arrays L and R
    let L = new Array(n1 + 1);
    let R = new Array(n2 + 1);

    // Copy data to the temporary arrays L and R
    for (let i = 0; i < n1; i++) {
        L[i] = A[p + i];
    }
    for (let j = 0; j < n2; j++) {
        R[j] = A[q + j + 1];
    }

    // Add sentinel values to the end of L and R
    L[n1] = Infinity;
    R[n2] = Infinity;

    // Initialize indices i and j
    let i = 0;
    let j = 0;

    // Merge the temporary arrays L and R back into A
    for (let k = p; k <= r; k++) {
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
    }
}

function mergeSort2(A, p, r) {
    if (p < r) {
        let q = Math.floor((p + r) / 2);
        mergeSort2(A, p, q);
        mergeSort2(A, q + 1, r);
        merge2(A, p, q, r);
    }
}



// test all
function testAll() {
    // assert
    const assert = require('assert');
    // test bogosort
    assert(BogoSorter.isSorted(BogoSorter.bogosort([1, 2, 3, 4, 5])));
    assert(BogoSorter.isSorted(BogoSorter.bogosort([5, 4, 3, 2, 1])));
    assert(BogoSorter.isSorted(BogoSorter.bogosort([1, 5, 2, 4, 3])));
    // test bubble sort
    assert(BogoSorter.isSorted(bubbleSort([1, 2, 3, 4, 5])));
    assert(BogoSorter.isSorted(bubbleSort([5, 4, 3, 2, 1])));
    assert(BogoSorter.isSorted(bubbleSort([1, 5, 2, 4, 3])));
    // test selection sort
    assert(BogoSorter.isSorted(selectionSort([1, 2, 3, 4, 5])));
    assert(BogoSorter.isSorted(selectionSort([5, 4, 3, 2, 1])));
    assert(BogoSorter.isSorted(selectionSort([1, 5, 2, 4, 3])));
    // test insertion sort
    assert(BogoSorter.isSorted(insertionSort([1, 2, 3, 4, 5])));
    assert(BogoSorter.isSorted(insertionSort([5, 4, 3, 2, 1])));
    assert(BogoSorter.isSorted(insertionSort([1, 5, 2, 4, 3])));

    assert(BogoSorter.isSorted(mergeSort([1, 2, 3, 4, 5])));
    assert(BogoSorter.isSorted(mergeSort([5, 4, 3, 2, 1])));
    assert(BogoSorter.isSorted(mergeSort([1, 5, 2, 4, 3])));

    assert(BogoSorter.isSorted(mergeSort2([1, 2, 3, 4, 5], 0, 4)));
    assert(BogoSorter.isSorted(mergeSort2([5, 4, 3, 2, 1], 0, 4)));
    assert(BogoSorter.isSorted(mergeSort2([1, 5, 2, 4, 3], 0, 4)));


    // log
    console.log("All tests passed.");
}
// Example usage:
// create random array of 100 elements
let unsortedArray = Array.from({ length: 100 }, () => Math.floor(Math.random() * 100));
// // time bogosort
// console.time('bogosort');
// const sortedArray = BogoSorter.bogosort(unsortedArray);
// console.timeEnd('bogosort');
// time bubble sort
console.time('bubbleSort');
const sortedArray2 = bubbleSort(unsortedArray);
console.timeEnd('bubbleSort');
// time selection sort
console.time('selectionSort');
const sortedArray3 = selectionSort(unsortedArray);
console.timeEnd('selectionSort');
// time insertion sort
console.time('insertionSort');
const sortedArray4 = insertionSort(unsortedArray);

console.timeEnd('insertionSort');
console.time('mergeSort');
const sortedArray5 = mergeSort(unsortedArray);
console.timeEnd('mergeSort');

testAll();