import 'dart:math';

List<int> countingSortByDigit(List<int> arr, int e) {
  List<int> count = List.filled(10, 0);
  for (int i = 0; i < arr.length; i++) {
    int digit = (arr[i] ~/ pow(10, e)) % 10;
    count[digit]++;
  }
  int offset = 0;
  for (int i = 0; i < count.length; i++) {
    int tmp = count[i];
    count[i] = offset;
    offset += tmp;
  }
  List<int> output = List.filled(arr.length, 0);
  for (int i = 0; i < arr.length; i++) {
    int digit = (arr[i] ~/ pow(10, e)) % 10;
    output[count[digit]] = arr[i];
    count[digit]++;
  }
  return output;
}

List<int> radixSort(List<int> arr, int max_digits) {
  for (int i = 0; i < max_digits; i++) {
    arr = countingSortByDigit(arr, i);
  }
  return arr;
}

List<int> smallestTrimmedNumbers(List<String> nums, List<List<int>> queries) {
  List<int> results = List.filled(queries.length, 0);
  for (int q = 0; q < queries.length; q++) {
    int k = queries[q][0];
    int trim = queries[q][1];
    List<int> trimmed = List<int>.generate(nums.length, (i) {
      String num = nums[i];
      if (num.length > trim) {
        num = num.substring(num.length - trim);
      }
      return int.parse(num);
    });

    // Sort the trimmed array using radix sort
    List<int> sortedTrimmed = radixSort(List.from(trimmed), trim);
    // check the index of sortedTrimmed[0] on trimmed array
    int index = trimmed.indexOf(sortedTrimmed[0]);
    results[q] = index;
  }
  return results;
}

void main() {
  List<String> nums = ["102", "473", "251", "814"];
  List<List<int>> queries = [
    [1, 1],
    [2, 3],
    [4, 2],
    [1, 2]
  ];
  print(smallestTrimmedNumbers(nums, queries));
}
