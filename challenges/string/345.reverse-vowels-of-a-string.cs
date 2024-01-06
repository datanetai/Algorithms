/*
 * @lc app=leetcode id=345 lang=csharp
 *
 * [345] Reverse Vowels of a String
 *
 * https://leetcode.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (51.63%)
 * Likes:    4274
 * Dislikes: 2726
 * Total Accepted:    710.3K
 * Total Submissions: 1.4M
 * Testcase Example:  '"hello"'
 *
 * Given a string s, reverse only all the vowels in the string and return it.
 * 
 * The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
 * lower and upper cases, more than once.
 * 
 * 
 * Example 1:
 * Input: s = "hello"
 * Output: "holle"
 * Example 2:
 * Input: s = "leetcode"
 * Output: "leotcede"
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 3 * 10^5
 * s consist of printable ASCII characters.
 * 
 * 
 */

// @lc code=start

public class Solution
{
    public string ReverseVowels(string s)
    {
        int i = 0, j = s.Length - 1;
        var vowels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u' };
        var chars = s.ToCharArray();
        while (i < j)
        {
            if (!vowels.Contains(char.ToLower(chars[i])))
            {
                i++;
                continue;
            }
            if (!vowels.Contains(char.ToLower(chars[j])))
            {
                j--;
                continue;
            }
            var temp = chars[i];
            chars[i] = chars[j];
            chars[j] = temp;
            i++;
            j--;
        }
        return new string(chars);
    }
}
// @lc code=end

