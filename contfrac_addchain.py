import math as m
import numpy as np
import math as m

def floor(num):
    return m.floor(num)

def ceil(num):
    return m.ceil(num)

def sign(n):
    if n < 0:
        return -1
    else:
        return 1



# Python program to demonstrate working of extended
# Euclidean Algorithm from geeks for geeks
# function for extended Euclidean Algorithm
def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

#TODO: I need to have the u1,u2 beforehand !!!
#this is an experimental gcf (it alternates between example 2.4 and 2.5, but produces correct result)
def gcf(n,k):
    gcd, a1, a2 = gcdExtended(n,k) # find a more elgant way to just extract a1 and a2 without gcd
    if a1 < 0:
        u1 = (-1)*a1*k
    else: 
        u1 = a1*k
        
    if (a1 < 0 and a2 < 0) or (a1 > 0 and a2 > 0):
        u2 = (-1)*(a2/a2)
        u2 = int(u2)
    elif (a1 < 0 and a2 > 0) or (a1 > 0 and a2 < 0):
        u2 = int((a2/a1))
    u = sorted([u1,u2])
    return u


def product(v,w):
    intermediate_result = np.multiply(w,v[-1]).tolist()
    v.extend(intermediate_result)
    return v

def addition(v,j):
    v.append(v[-1]+j)
    return v


def subtraction(v,j):
    v.append(v[-1]-j)
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
        return sorted(list(set(product(minchain(k),minchain(q)))))
    else:
         return sorted(list(set(addition(product(chain(k,r),minchain(q)),r))))
         



