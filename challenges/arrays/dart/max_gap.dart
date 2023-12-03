class Solution {
  int maximumGap(List<int> nums) {
    if (nums.length < 2) {
      return 0;
    }
    radixSort(nums);
    var maxGap = 0;
    for (var i = 0; i < nums.length - 1; i++) {
      var diff = nums[i + 1] - nums[i];
      if (abs(diff) > maxGap) {
        maxGap = abs(diff);
      }
    }
    return maxGap;
  }

  int abs(int a) {
    return a < 0 ? -a : a;
  }
}

void radixSort(List<int> nums) {
  var maxElement = nums.reduce((a, b) => a > b ? a : b);
  var exp = 1;
  while (maxElement / exp > 0) {
    countingSortbyDigit(nums, exp);
    exp *= 10;
  }
}

void countingSortbyDigit(List<int> nums, int exp) {
  var count = List<int>.filled(10, 0);
  var output = List<int>.filled(nums.length, 0);
  for (var i = 0; i < nums.length; i++) {
    count[(nums[i] / exp).floor() % 10]++;
  }
  for (var i = 1; i < 10; i++) {
    count[i] += count[i - 1];
  }
  for (var i = nums.length - 1; i >= 0; i--) {
    output[count[(nums[i] / exp).floor() % 10] - 1] = nums[i];
    count[(nums[i] / exp).floor() % 10]--;
  }
  for (var i = 0; i < nums.length; i++) {
    nums[i] = output[i];
  }
}

void main() {
  var solution = Solution();
  var nums = [3, 6, 9, 1];
  print(solution.maximumGap(nums));
}
