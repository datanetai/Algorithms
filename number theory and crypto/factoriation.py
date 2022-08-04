
import math
def fermatfactor(n):
    """
    Fermat's factorization method
    """
    a=math.ceil(math.sqrt(n))
    b2=a*a-n
    while not is_square(b2):
        a+=1
        b2=a*a-n
    return a-math.sqrt(b2),a+math.sqrt(b2)

def is_square(n):
    """
    Check if n is a perfect square
    """
    sr=math.sqrt(n)
    return sr==int(sr)

#test fermatfactor
print(fermatfactor(5003))