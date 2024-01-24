    /*
    * @lc app=leetcode id=1657 lang=typescript
    *
    * [1657] Determine if Two Strings Are Close
    *
    * https://leetcode.com/problems/determine-if-two-strings-are-close/description/
    *
    * algorithms
    * Medium (53.74%)
    * Likes:    3486
    * Dislikes: 242
    * Total Accepted:    281.7K
    * Total Submissions: 506.7K
    * Testcase Example:  '"abc"\n"bca"'
    *
    * Two strings are considered close if you can attain one from the other using
    * the following operations:
    * 
    * 
    * Operation 1: Swap any two existing characters.
    * 
    * 
    * For example, abcde -> aecdb
    * 
    * 
    * Operation 2: Transform every occurrence of one existing character into
    * another existing character, and do the same with the other
    * character.
    * 
    * For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into
    * a's)
    * 
    * 
    * 
    * 
    * You can use the operations on either string as many times as necessary.
    * 
    * Given two strings, word1 and word2, return true if word1 and word2 are
    * close, and false otherwise.
    * 
    * 
    * Example 1:
    * 
    * 
    * Input: word1 = "abc", word2 = "bca"
    * Output: true
    * Explanation: You can attain word2 from word1 in 2 operations.
    * Apply Operation 1: "abc" -> "acb"
    * Apply Operation 1: "acb" -> "bca"
    * 
    * 
    * Example 2:
    * 
    * 
    * Input: word1 = "a", word2 = "aa"
    * Output: false
    * Explanation: It is impossible to attain word2 from word1, or vice versa, in
    * any number of operations.
    * 
    * 
    * Example 3:
    * 
    * 
    * Input: word1 = "cabbba", word2 = "abbccc"
    * Output: true
    * Explanation: You can attain word2 from word1 in 3 operations.
    * Apply Operation 1: "cabbba" -> "caabbb"
    * Apply Operation 2: "caabbb" -> "baaccc"
    * Apply Operation 2: "baaccc" -> "abbccc"
    * 
    * 
    * 
    * Constraints:
    * 
    * 
    * 1 <= word1.length, word2.length <= 10^5
    * word1 and word2 contain only lowercase English letters.
    * 
    * 
    */

    // @lc code=start
    function closeStrings(word1: string, word2: string): boolean {
        let count1 = new Map()
        let count2 = new Map()
        for (let i = 0; i < word1.length; i++) {
            count1.set(word1[i], (count1.get(word1[i]) || 0) + 1)
        }
        for (let i = 0; i < word2.length; i++) {
            count2.set(word2[i], (count2.get(word2[i]) || 0) + 1)
        }
        let key1 = [...count1.keys()].sort()
        let key2 = [...count2.keys()].sort()

        let value1 = [...count1.values()].sort()
        let value2 = [...count2.values()].sort()
        return key1.join('') === key2.join('') && value1.join('') === value2.join('')
    };
    // @lc code=end

