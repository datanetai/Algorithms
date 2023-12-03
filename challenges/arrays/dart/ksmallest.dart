// You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.

// You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:

// Trim each number in nums to its rightmost trimi digits.
// Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.
// Reset each number in nums to its original lengt
class Pair {
  int index;
  String value;
  Pair({required this.index, required this.value});
}

class Solution {
  List<int> smallestTrimmedNumbers(List<String> nums, List<List<int>> queries) {
    List<int> result = List.filled(queries.length, 0);
    for (int i = 0; i < queries.length; i++) {
      List<Pair> arr = List.filled(nums.length, Pair(0, ""));
      for (int j = 0; j < nums.length; j++) {
        int start = nums[j].length - queries[i][1];
        arr[j] = Pair(j, nums[j].substring(start));
      }
      radixSort(arr);
      result[i] = arr[queries[i][0] - 1].index;
    }
    return result;
  }

  void radixSort(List<Pair> arr) {
    var maxlen = 0;
    int n = arr.length;
    for (int i = 0; i < n; i++) {
      if (arr[i].value.length > maxlen) {
        maxlen = arr[i].value.length;
      }
    }
    // do counting sort for every digit. Note that instead
    // of passing digit number, exp is passed. exp is 10^i
    // where i is current digit number
    int exp = 1;
    while (maxlen > 0) {
      countingSort(arr, exp);
      exp *= 10;
      maxlen--;
    }
  }

  void countingSort(List<Pair> pairs, int digit) {
    List<int> counts = List.filled(10, 0);
    List<Pair> output = List.filled(pairs.length, Pair(0, ""));

    // Count digit occurrences at the current position
    for (var pair in pairs) {
      int d = charAt(pair.value, digit);
      counts[d]++;
    }

    // Cumulative count
    for (int i = 1; i < 10; i++) {
      counts[i] += counts[i - 1];
    }

    // Build the sorted array
    for (int i = pairs.length - 1; i >= 0; i--) {
      int d = charAt(pairs[i].value, digit);
      output[counts[d] - 1] = pairs[i];
      counts[d]--;
    }

    // Copy back to the original array
    for (int i = 0; i < pairs.length; i++) {
      pairs[i] = output[i];
    }
  }

  // charAt returns the digit at the specified position from the right, or 0 if out of range
  int charAt(String s, int pos) {
    if (pos < s.length) {
      return int.parse(s[s.length - 1 - pos]);
    }
    return 0; // Shorter strings are treated as if they have leading zeros
  }
}
