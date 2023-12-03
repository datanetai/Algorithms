class Solution {
  int strStr(String haystack, String needle) {
    int i = 0;
    int j = 0;
    int start = 0;
    for (i = 0; i < haystack.length; i++) {
      if (haystack[i] == needle[j]) {
        if (j == 0) {
          start = i;
        }
        j++;
      } else {
        if (j > 0) {
            i = start;
        }
        j = 0;
      }
      if (j == needle.length) {
        return start;
      }
    }
    return -1;
  }
}
