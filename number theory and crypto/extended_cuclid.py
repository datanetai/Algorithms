# extended euclid

def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (g, x, y) = extended_euclid(b, a % b)
        return (g, y, x - (a // b) * y)

def extended_euclid_iterative(a, b):
    #s and t
    # r(i-1)=q(i-1)*r(i)+r(i+1)
    old_s,s=1,0
    old_t,t=0,1
    while b != 0:
        q, r = divmod(a, b)
        print(q,r)
        a, b = b, r
        old_s,s = s, old_s - q * s
        old_t,t = t, old_t - q * t
    return (a, old_s, old_t)
print(extended_euclid_iterative(7,23))