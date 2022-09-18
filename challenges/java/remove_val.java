class Solution {
    public int removeElement(int[] nums, int val) {
       count = 0;
         for(int i = 0; i < nums.length; i++){
              if(nums[i] != val){
                nums[count] = nums[i];
                count++;
              }
         }
            return count;
    }
    public static void main(Stirng[] args) {
        int[] nums = {3,2,2,3};
        int val = 3;
        Solution sol = new Solution();
        System.out.println(sol.removeElement(nums, val));
    }
}