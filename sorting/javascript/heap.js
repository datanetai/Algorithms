// heap implementation
function left(i) {
    return 2 * i + 1;
}
function right(i) {
    return 2 * i + 2;
}
function parent(i) {
    return Math.floor((i - 1) / 2);
}


function maxHeapify(A, i, heapSize) {
    let l = left(i);
    let r = right(i);
    let largest;

    if (l < heapSize && A[l] > A[i]) {
        largest = l;
    } else {
        largest = i;
    }
    if (r < heapSize && A[r] > A[largest]) {
        largest = r;
    }
    if (largest !== i) {
        let temp = A[i];
        A[i] = A[largest];
        A[largest] = temp;
        maxHeapify(A, largest, heapSize);
    }
}

function buildMaxHeap(A) {
    let heapSize = A.length;
    for (let i = Math.floor((A.length - 1) / 2); i >= 0; i--) {
        maxHeapify(A, i, heapSize);
    }
}

function heapSort(A) {
    buildMaxHeap(A);
    let heapSize = A.length;
    for (let i = A.length - 1; i >= 1; i--) {
        let temp = A[0];
        A[0] = A[i];
        A[i] = temp;
        heapSize--;
        maxHeapify(A, 0, heapSize);
    }
}

// test
let A = [9, 9, 7, 6, 5, 4, 3, 22, 1];
buildMaxHeap(A);
console.log(A);
heapSort(A);
console.log(A);




