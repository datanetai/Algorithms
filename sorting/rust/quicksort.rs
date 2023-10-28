// quicksort

fn partition (arr: &mut [i32], low:i32, high:i32) -> i32 {
    let pivot = arr[high as usize];
    let mut i = low - 1;
    for j in low..high{
        if arr[j as usize] < pivot {
            i += 1;
            arr.swap(i as usize, j as usize);
        }
    }
    arr.swap((i+1) as usize, high as usize);
    return i+1;
}
fn quicksort (arr: &mut [i32], low:i32, high:i32) {
    if low < high {
        let pi = partition(arr, low, high);
        quicksort(arr, low, pi-1);
        quicksort(arr, pi+1, high);
    }
}

fn main() {
    let mut arr = [10, 7, 8, 9, 1, 5];
    let n = arr.len() as i32;
    quicksort(&mut arr, 0, n-1);
    println!("Sorted array is {:?}", arr);
}