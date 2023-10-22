public class SortingAlgorithms {
    public static void main(String[] args) {
        System.out.println("bubble sort");
        int[] arr = { 5, 4, 3, 2, 1 };
        bubbleSort(arr);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
        }
        System.out.println("insertion sort");
        // insertionSort
        int[] arr2 = { 5, 4, 3, 2, 1 };
        insertionSort(arr2);
        for (int i = 0; i < arr2.length; i++) {
            System.out.print(arr2[i]);
        }
        System.out.println("merge sort");

        // mergeSort
        int[] arr3 = { 5, 4, 3, 2, 1 };
        arr3 = mergeSort(arr3);
        for (int i = 0; i < arr3.length; i++) {
            System.out.print(arr3[i]);
        }
    }

    public static int[] bubbleSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = arr.length - 1; j > i; j--) {
                if (arr[j] < arr[j - 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = temp;
                }
            }
        }
        return arr;
    }

    // sort from end bubbleSort
    public static int[] bubbleSort2(int[] arr) {
        for (int i = arr.length - 1; i >= 0; i--) {
            for (int j = 0; j < i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j + 1];
                    arr[j + 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        return arr;
    }

    // selection sort
    public static int[] selectionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int min = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[min]) {
                    min = j;
                }
            }
            int temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
        return arr;
    }

    public static int[] insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int j = i;
            int current = arr[i];
            while (j > 0 && arr[j - 1] > current) {
                arr[j] = arr[j - 1];
                j--;
            }
            arr[j] = current;
        }
        return arr;
    }

    public static int[] merge(int[] left_arr, int[] right_array) {
        int left_index = 0;
        int right_index = 0;
        int[] result = new int[left_arr.length + right_array.length];
        while (left_index < left_arr.length && right_index < right_array.length) {
            if (left_arr[left_index] < right_array[right_index]) {
                result[left_index + right_index] = left_arr[left_index];
                left_index++;
            } else {
                result[left_index + right_index] = right_array[right_index];
                right_index++;
            }
        }
        while (left_index < left_arr.length) {
            result[left_index + right_index] = left_arr[left_index];
            left_index++;
        }
        while (right_index < right_array.length) {
            result[left_index + right_index] = right_array[right_index];
            right_index++;
        }
        return result;
    }

    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }
        int mid = arr.length / 2;
        int[] left_arr = new int[mid];
        int[] right_arr = new int[arr.length - mid];
        for (int i = 0; i < mid; i++) {
            left_arr[i] = arr[i];
        }
        for (int i = mid; i < arr.length; i++) {
            right_arr[i - mid] = arr[i];
        }
        left_arr = mergeSort(left_arr);
        right_arr = mergeSort(right_arr);

        return merge(left_arr, right_arr);

    }

}