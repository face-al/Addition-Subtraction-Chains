import math as m
import numpy as np

def floor(num):
    m.floor(num)
    return num

def NAF(x):
    if x == 0:
        return []
    z = 0 if x % 2 == 0 else 2 - (x % 4)
    return NAF( (x-z) // 2 ) + [z]

def product(v,w):
    intermediate_result = np.multiply(v,w).tolist()
    v.extend(intermediate_result)
    return v

def addition(v,j):
    v.append(v[-1]+j)
    return v

def minchain(n):
    l = len(n)
    if n == 2**l:
        return [2**i for i in range(l)]
    if n == 3:
        return [1,2,3]
    return chain(n, 2**m.log(n/2))

def log_2(x):
    m.log2(x)
    return x

def alpha(n):
    return floor(n / 2**m.ceil(floor(log_2(n)/2)))
    
def chain(n,k):
    q, r = floor(n/k), n % k
    if r == 0:
        return product(minchain(k),minchain(q))
    else:
        return addition(product(chain(k,r)+ minchain(q)), r)



