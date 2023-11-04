
class Solution {
  // Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
  List<int> intersection(List<int> nums1, List<int> nums2) {
    List<int> result = [];
    Set<int> set = Set.from(nums1);
    for (int i=0; i<nums2.length; i++){
        if (set.contains(nums2[i])){
            result.add(nums2[i]);
                set.remove(nums2[i]);
        }
    }
    return result;
  }
//   Time complexity : O(n+m) for both solutions
List<int> intersection2(List<int> nums1, List<int> nums2) {
    // convert to set 
    Set<int> set1 = Set.from(nums1);
    Set<int> set2 = Set.from(nums2);
    // find the smaller set
    if (set1.length < set2.length) {
      return set_intersection(set1, set2);
    } else {
      return set_intersection(set2, set1);
    }

  }
  List<int> set_intersection(Set<int> set1, Set<int> set2) {
    // set 1 is the smaller set
    List<int> result = [];
    for (int s in set1) {
      if (set2.contains(s)) {
        result.add(s);
      }
    }
    return result;
    
  }
//   Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
// complexity O(nlogn + mlogm)
List<int> intersect(List<int> nums1, List<int> nums2) {
    // sort both arrays
    nums1.sort();
    nums2.sort();
    int i = 0, j = 0;
    List<int> result = [];
    while (i < nums1.length && j < nums2.length){
        if(nums1[i] == nums2[j]){
            result.add(nums1[i]);
            i++;
            j++;
        }
        else if(nums1[i]<nums2[j]){
            i++;
        }
        else{
            j++;
        }
    }
    return result;
  }
  // approach 2 complexity O(n+m)
     List<int> intersect2(List<int> nums1, List<int> nums2){
        Map<int, int> count = {};
      for (int i=0; i<nums1.length; i++){
          if (count.containsKey(nums1[i])) {
        int currentValue = count[nums1[i]]!;
        count[nums1[i]] = currentValue + 1;
    } else {
        count[nums1[i]] = 1;
    }
      }
      List<int> result = [];
      for (int i=0; i<nums2.length; i++){
          if(count.containsKey(nums2[i]) && count[nums2[i]]!>0){
              result.add(nums2[i]);
              int currentValue = count[nums2[i]]!;
              count[nums2[i]] = currentValue - 1;
          }
      }
      return result;
  }
  void test() {
    print(intersection([1,2,2,1], [2,2]));
    print(intersection2([1,2,2,1], [2,2]));
    print(intersect([1,2,2,1], [2,2]));
    print(intersect2([1,2,2,1], [2,2]));
  }
}
void main() {
  Solution sol = Solution();
  sol.test();
}