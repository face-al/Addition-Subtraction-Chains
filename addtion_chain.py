import math as m
import numpy as np

def floor(num):
    return m.floor(num)

def ceil(num):
    return m.ceil(num)

def NAF(x):
    if x == 0:
        return []
    z = 0 if x % 2 == 0 else 2 - (x % 4)
    return NAF( (x-z) // 2 ) + [z]

def product(v,w):
    intermediate_result = np.multiply(w,v[-1]).tolist()
    v.extend(intermediate_result)
    return v

def addition(v,j):
    v.append(v[-1]+j)
    return v

def log_2(x):
    result = 0
    while x > 1:
        x >>= 1
        result += 1
    return result

def alpha(n):
    fraction = 1 << int(ceil(floor(log_2(n))/2))
    return floor(n/fraction)

def minchain(n):
    l = n.bit_length() - 1 
    if n == 1<<l:
        return [2**(i) for i in range(l+1)]
    if n == 3:
        return [1,2,3]
    return chain(n, 1 << floor(log_2(int(n/2))))

  
def chain(n,k):
    q = floor(n/k)
    r = n % k
    if r == 0:
        return product(minchain(k),minchain(q))
    else:
        min_ac_chain = addition(product(chain(k,r),minchain(q)),r)
        min_ac_chain = [*set(min_ac_chain)]
        return min_ac_chain



