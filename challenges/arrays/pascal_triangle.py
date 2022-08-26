# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1],[1,1]]
    result = [[1],[1,1]]
    for i in range(2,numRows):
        result.append([1])
        for j in range(1,i):
            result[i].append(result[i-1][j-1]+result[i-1][j])
        result[i].append(1)
    return result

# O(n) solution (Any row can be constructed using the offset sum of the previous row)
def generate2( numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [[1]]
    for i in range(1, numRows):
        res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
    return res[:numRows]

# same solution but without map
def generate3( numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [[1]]
    for i in range(1, numRows):
        tmp1 = [0] + res[-1]
        tmp2 = res[-1] + [0]
        res.append([tmp1[i]+tmp2[i] for i in range(len(tmp1))])
    return res[:numRows]



