/*
 * @lc app=leetcode id=399 lang=typescript
 *
 * [399] Evaluate Division
 *
 * https://leetcode.com/problems/evaluate-division/description/
 *
 * algorithms
 * Medium (61.43%)
 * Likes:    9008
 * Dislikes: 874
 * Total Accepted:    446.6K
 * Total Submissions: 725.8K
 * Testcase Example:  '[["a","b"],["b","c"]]\n' +
  '[2.0,3.0]\n' +
  '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
 *
 * You are given an array of variable pairs equations and an array of real
 * numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
 * equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
 * single variable.
 * 
 * You are also given some queries, where queries[j] = [Cj, Dj] represents the
 * j^th query where you must find the answer for Cj / Dj = ?.
 * 
 * Return the answers to all queries. If a single answer cannot be determined,
 * return -1.0.
 * 
 * Note: The input is always valid. You may assume that evaluating the queries
 * will not result in division by zero and that there is no contradiction.
 * 
 * Note: The variables that do not occur in the list of equations are
 * undefined, so the answer cannot be determined for them.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
 * [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
 * Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
 * Explanation: 
 * Given: a / b = 2.0, b / c = 3.0
 * queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
 * return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
 * note: x is undefined => -1.0
 * 
 * Example 2:
 * 
 * 
 * Input: equations = [["a","b"],["b","c"],["bc","cd"]], values =
 * [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
 * Output: [3.75000,0.40000,5.00000,0.20000]
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: equations = [["a","b"]], values = [0.5], queries =
 * [["a","b"],["b","a"],["a","c"],["x","y"]]
 * Output: [0.50000,2.00000,-1.00000,-1.00000]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= equations.length <= 20
 * equations[i].length == 2
 * 1 <= Ai.length, Bi.length <= 5
 * values.length == equations.length
 * 0.0 < values[i] <= 20.0
 * 1 <= queries.length <= 20
 * queries[i].length == 2
 * 1 <= Cj.length, Dj.length <= 5
 * Ai, Bi, Cj, Dj consist of lower case English letters and digits.
 * 
 * 
 */

// @lc code=start
function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    let graph = new Map<string, Map<string, number>>();
    let result: number[] = []
    for (let i = 0; i < equations.length; i++) {
        let [a, b] = equations[i]
        let value = values[i]
        if (!graph.has(a)) {
            graph.set(a, new Map())
        }
        if (!graph.has(b)) {
            graph.set(b, new Map());
        }
        (graph.get(a) as Map<string, number>).set(b, value);
        (graph.get(b) as Map<string, number>).set(a, 1 / value);
    }
    function dfs(start: string, end: string, visited: Set<string>) {
        if (!graph.has(start)) return -1;
        if (graph.get(start).has(end)) return graph.get(start).get(end);
        visited.add(start);
        for (let [node, value] of graph.get(start) as Map<string, number>) {
            if (visited.has(node)) continue;
            let result = dfs(node, end, visited);
            if (result != -1) {
                graph.get(start).set(end, value * result);
                return value * result;
            }
        }
        return -1;
    }
    for (let [start, end] of queries) {
        result.push(dfs(start, end, new Set()));
    }
    return result;
};
// @lc code=end

