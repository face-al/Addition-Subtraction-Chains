# import addtion_chain as ac
import contfrac as cf
import math as m
import numpy as np

# Python program to demonstrate working of extended
# Euclidean Algorithm from geeks for geeks
    
    
    
#TODO: I need to have the u1,u2 beforehand !!!

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


# ax + by = gcd(a,b)
# GOAL: a/b 
#STEP 1: ax = gcd(a,b) + (-1)*by
#STEP 2: a/b = gcd(a,b)/bx + (-1)* y/x
#STEP 3: u1 = (-1)*(y/x), u2 = np.sign(gcd(a,b)/bx)*bx
# n = 55
# k = 28


# print(a1,a2)
# if a1 < 0:
#     u1 = a1*k
# else: 
#     u1 = a1*k
 
# if (a1 < 0 and a2 < 0) or (a1 > 0 and a2 > 0):
#     u2 = (-1)*(a2/a2)
#     u2 = int(u2)
# elif (a1 < 0 and a2 > 0) or (a1 > 0 and a2 < 0):
#     u2 = int((-1)*(a2/a1))
    
# u = [u1,u2]
# print(u)

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

# print(gcf(55,28))
# print(gcf(55,7))
# n = 55
# k = 7
# gcd, a1, a2 = gcdExtended(n,k)

# print(a1,a2)
# if a1 < 0:
#     u1 = a1*k
# else: 
#     u1 = a1*k
 
# if (a1 < 0 and a2 < 0) or (a1 > 0 and a2 > 0):
#     u2 = (-1)*(a2/a2)
#     u2 = int(u2)
# elif (a1 < 0 and a2 > 0) or (a1 > 0 and a2 < 0):
#     u2 = int((-1)*(a2/a1))
    
# u = [u1,u2]
# print(u)
    
# print(x,y)







#implementaion of amadou 2013 paper, generalized cf for as-chains
#strategy chosen is square root strategy
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

# strategy choose a prefined method, then generalize
# here we chose square root method strategy
def minchain(n):
    l = n.bit_length() - 1 
    res = []
    if n == 1<<l:
        return [2**(i) for i in range(l+1)]
    if n == 3:
        return [1,2,3]
    else:
        #line 7 from p.7, using square root method
        k = m.floor(m.sqrt(n))
        return chain(n,k)



def sign(n):
    if n < 0:
        return -1
    else:
        return 1
    
    
    
def chain(n,k):
    u = gcf(n,k)
    print("u: ",u)
    q0 = m.gcd(n,k)
    print("q0: ", q0)
    q1 = abs(u[0])*q0
    print("q1: ",q1)
    x0 = minchain(abs(q0))
    print("x0: ", x0)
    x1 = product(x0,minchain(abs(u[0])))
    print("x1: ",x1)
    # return
    #should be a loop here but r =2
    # q2 = abs(u[1])*q1 +sign(u[0])*q0
    
    # print(res)
    x2 = product(x1,minchain(abs(u[1])))
    print("x2: ", x2)
    
    if(u[0] < 0):
        x2 = subtraction(x2,q0)
        print("x2: (subtraction) ", x2)

    else:
        x2 = addition(x2,q0)
        print("x2: (addition)", x2)

    return x2

print(chain(55,28))





