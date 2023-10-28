// quicksort implementation

int partition(List<int> arr, int low, int high){
    int pivot = arr[high];
    int i = low - 1;
    for (int j=low;j<high;j++){
        if (arr[j]<pivot){
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

    }
    int temp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = temp;
    return i+1;
}

void quicksort(List<int> arr, int low, int high){
    if (low<high){
        int pi = partition(arr, low, high);
        quicksort(arr, low, pi-1);
        quicksort(arr, pi+1, high);
    }
}

void main(){
    List<int> arr = [10, 7, 8, 9, 1, 5];
    int n = arr.length;
    quicksort(arr, 0, n-1);
    print(arr);
}