# shanker's baby step giant step
import math
def baby_step_giant_step(g,h,p):
    ord=order_of(g,p)
    n=math.floor(math.sqrt(ord))+1
    list1=[]
    list2=[]
    u=pow(g,-n,p)
    for i in range(n+1):
        list1.append(pow(g,i,p))
        list2.append(h*pow(u,i)%p)
    #find match
    #we should use fast searching method
    # otherwise the complexity will be O(N**2)
    #first sort both list then apply merge sort like procedure to find comman element
    
    for i in range(n+1):
        for j in range(n+1):
            if list1[i]==list2[j]:
                return i+j*n
    return -1
    

def order_of(g,p):
    ord=0
    for i in range(1,p):
        if pow(g,i,p)==1:
            ord=i
            break
    return ord



g=9704
h=13896
p=17389
print(baby_step_giant_step(g,h,p))