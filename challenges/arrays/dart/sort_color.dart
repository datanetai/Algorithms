class Solution {
  void sortColors(List<int> nums) {
     List<int> freq = List.filled(3, 0);
     for (int i = 0; i < nums.length; i++) {
       freq[nums[i]]++;
     }
    // commulative sum
    for (int i = 1; i < freq.length; i++) {
      freq[i] += freq[i - 1];
    }
    List<int> sortedNums = List.filled(nums.length, 0);
    for (int i = nums.length - 1; i >= 0; i--) {
      sortedNums[freq[nums[i]] - 1] = nums[i];
      freq[nums[i]]--;
    }
    nums.setAll(0, sortedNums);
  }
 // since only numbers are 0,1 and 2 so we can maintain count of each number and then set the array
  void sortColors2(List<int> nums) {
     List<int> count = List.filled(3, 0);
        for (int i = 0; i < nums.length; i++) {
        count[nums[i]]++;
        }
        // iterate over count array and set the values in nums
        int index = 0;
        for (int i = 0; i < count.length; i++) {
            for (int j = 0; j < count[i]; j++) {
                nums[index++] = i;
            }
        }

// dutch national flag algorithm
   void sortColors3(List<int> nums) {
    int low = 0;
    int mid = 0;
    int high = nums.length - 1;
    while (mid <= high) {
      if (nums[mid] == 0) {
        swap(nums, low, mid);
        low++;
        mid++;
      } else if (nums[mid] == 1) {
        mid++;
      } else {
        swap(nums, mid, high);
        high--;
      }
    }
  }

  void swap(List<int> nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
  }

 // same as above but more optimized for this problem
 void sortColors4(List<int> nums) {
    int low = 0;
    int mid = 0;
    int high = nums.length - 1;
    while (mid <= high) {
      if (nums[mid] == 0) {
        int temp = nums[low];
        nums[low] = 0;
        nums[mid] = temp;
        low++;
        mid++;
      } else if (nums[mid] == 1) {
        mid++;
      } else {
        int temp = nums[high];
        nums[high] = 2;
        nums[mid] = temp;
        high--;
      }
    }
  }
}
