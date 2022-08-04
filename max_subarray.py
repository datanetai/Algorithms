import math
# import sys
# sys.setrecursionlimit(15000)

def max_subarray(A):
    max=0
    lefti,rightj=0,0
    #running time O(n**2) using running sum
    for i in range(len(A)):
        sum=0
        for j in range(i,len(A)):
            sum+=A[j]
            if sum>max:
                lefti,rightj=i,j
                max=sum
    return (lefti,rightj,max)

#efficient solution
def find_max_crossing_subarray(A,low,mid,high):
    left_sum=0
    sum=0
    max_left=mid
    for i in range(mid,low-1,-1):
        sum+=A[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i
    right_sum=0
    sum=0
    max_right=mid
    for j in range(mid+1,high+1):
        sum+=A[j]
        if sum>right_sum:
            right_sum=sum
            max_right=j
    return (max_left,max_right,left_sum+right_sum)

def find_maximum_subarray(A,low,high):
    if high==low:
        print(low)
        return (low,high,A[low])
    else:
        mid= math.floor((low+high)/2)
        left_low,left_high,left_sum=find_maximum_subarray(A,low,mid)
        right_low,right_high,right_sum=find_maximum_subarray(A,mid+1,high)
        cross_low,cross_high,cross_sum=find_max_crossing_subarray(A,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>=left_sum and right_sum>=cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)

A=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

print(find_maximum_subarray(A,0,len(A)-1))