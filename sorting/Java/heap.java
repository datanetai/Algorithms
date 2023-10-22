
public class Main {
    public static void main(String[] args) {
        System.out.println("heap sort");
        // create array of hundred random numbers
        int[] arr = new int[100];
        for (int i = 0; i < arr.length; i++) {
            // random number between 0 and 100
            arr[i] = (int) (Math.random() * 100);
        }
        Heap heap = new Heap(arr);
        heap.heapSort();
        heap.printHeap();
    }

}

public class Heap {
    // define types amd constructor
    private int[] heap;
    private int size;

    public Heap(int[] arr) {
        heap = arr;
        size = arr.length;
    }

    public int left(int i) {
        return 2 * i + 1;
    }

    public int right(int i) {
        return 2 * i + 2;
    }

    public int parent(int i) {
        return (i - 1) / 2;
    }

    public void maxHeapify(int i) {
        int l = left(i);
        int r = right(i);
        int largest = i;
        if (l < size && heap[l] > heap[largest])
            largest = l;
        if (r < size && heap[r] > heap[largest])
            largest = r;
        if (largest != i) {
            int temp = heap[i];
            heap[i] = heap[largest];
            heap[largest] = temp;
            maxHeapify(largest);
        }
    }

    public void buildMaxHeap() {
        for (int i = size / 2; i >= 0; i--) {
            maxHeapify(i);
        }
    }

    public void heapSort() {
        buildMaxHeap();
        for (int i = size - 1; i >= 0; i--) {
            int temp = heap[0];
            heap[0] = heap[i];
            heap[i] = temp;
            size--;
            maxHeapify(0);
        }
    }

    public void printHeap() {
        for (int i = 0; i < heap.length; i++) {
            System.out.print(heap[i] + " ");
        }
    }

}