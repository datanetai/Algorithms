#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    // complexity: O(n) but higher constant factor
    // solution 1 brute force naive
    void moveZeroes(vector<int> &nums)
    {
        int zeros = 0;
        // count the number of zeros
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 0)
            {
                zeros++;
            }
        }
        // move all non-zero elements to the front
        for (int i = 0, j = 0; i < nums.size(); i++)
        {
            if (nums[i] != 0)
            {
                nums[j] = nums[i];
                j++;
            }
        }
        // fill the remaining elements with zeros
        for (int i = nums.size() - zeros; i < nums.size(); i++)
        {
            nums[i] = 0;
        }
    }

    // solution 2 two pointers
    void moveZeroes2(vector<int> &nums)
    {
        int i = 0, j = i + 1;
        for (; i < nums.size() && j < nums.size();)
        {
            if (nums[i] == 0 && nums[j] != 0)
            {
                swap(nums[i], nums[j]);
                i++;
                j++;
            }
            else if (nums[i] == 0 && nums[j] == 0)
            {
                j++;
            }
            else
            {
                i++;
                j++;
            }
        }
    }

    // solution 3 snowball approach
    void moveZeroes3(vector<int> &nums)
    {
        int snowballSize = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 0)
            {
                snowballSize++;
            }
            else if (snowballSize > 0)
            {
                swap(nums[i], nums[i - snowballSize]);
            }
        }
    }
};

int main()
{
    Solution solution;
    vector<int> nums = {3, 0, 1, 0, 2, 0, 4};
    solution.moveZeroes2(nums);
    for (int i = 0; i < nums.size(); i++)
    {
        cout << nums[i] << " ";
    }
}