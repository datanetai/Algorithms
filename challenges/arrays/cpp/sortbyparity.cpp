#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> sortArrayByParity(vector<int> &nums)
    {

        for (int i = 0, even = 0; i < nums.size(); i++)
        {
            if ((nums[i] & 1) == 0)
            {
                swap(nums[i], nums[even]);
                even++;
            }
        }
        return nums;
    }
};
// solution 2
vector<int> sortArrayByParity2(vector<int> &nums)
{
    int start = 0, end = nums.size();
    while (start < end)
    {
        if (nums[end] % 2 == 0)
        {
            swap(nums[start], nums[end]);
            start++;
            end--;
        }
        else if (nums[start] % 2 == 0)
        {
            end--;
        }
        else
        {
            start++;
        }
    }
}


int main()
{
    Solution solution;
    vector<int> nums = {3, 1, 2, 4};
    vector<int> result = solution.sortArrayByParity(nums);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << "wew ";
    }
}
