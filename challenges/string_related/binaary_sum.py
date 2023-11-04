# Given two binary strings a and b, return their sum as a binary string.
# solution O(n).
def addBinary( a: str, b: str) -> str:
        res = ''
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry == 1:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res = str(carry % 2) + res
            carry //= 2
        return res

# recursive solution same complexity O(m+n+c)  c="count of carries, which is less than min(m,n)"
def addBinary(a: str, b: str) -> str:
    if a == '':
        return b
    if b == '':
        return a
    if a[-1] == '1' and b[-1] == '1':
        return addBinary(addBinary(a[:-1], b[:-1]), '1') + '0'
    if a[-1] == '0' and b[-1] == '0':
        return addBinary(a[:-1], b[:-1]) + '0'
    return addBinary(a[:-1], b[:-1]) + '1'
        