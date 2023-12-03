// Given two binary strings a and b, return their sum as a binary string.

// Example 1:

// Input: a = "11", b = "1"
// Output: "100"
class Solution {
  String addBinary(String a, String b) {
    int sum = 0;
    int carry = 0;
    int i = a.length - 1;
    int j = b.length - 1;
    String result = "";
    while (i >= 0 || j >= 0) {
      sum = carry;
      if (i >= 0) {
        sum += int.parse(a[i]);
      }
      if (j >= 0) {
        sum += int.parse(b[j]);
      }
      result = (sum % 2).toString() + result;
      carry = sum ~/ 2;
      i--;
      j--;
    }
    if (carry != 0) {
      result = carry.toString() + result;
    }
    return result;
  }
}

void main() {
  Solution solution = Solution();
  print(solution.addBinary("11", "1"));
}
