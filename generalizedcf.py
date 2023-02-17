# import addtion_chain as ac
import contfrac as cf
import math as m

#TODO: define your own cf and dont use contfrac

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
    else:
        if n == 3:
            return [1,2,3]
        else:
            #line 7 from p.7, using square root method
            k = m.floor(m.sqrt(n))
            res = chain(n,k)
    return res

def chain(n,k):
    value = n/k
    # strategy = m.floor(m.sqrt(n)) #using squared method
    coefficient = list(cf.continued_fraction(value)) 
    r = len(coefficient)
    Q = [m.gcd(n,k)]
    Q.append(coefficient[0]*Q[0])  
    X_0 = minchain(Q[0]) #use square root method
    X_1 = product(X_0, minchain(coefficient[0]))
    X = [X_0, X_1]
    for i in range(2,len(coefficients)):
        Q[i] = Q[i-1] + Q[i-2]
        X[i] = product(X[i-1],minchain(coefficient[i]))
        if (coefficient[i-1] < 0):
            X[i] = subtraction(X[i],Q[i-2])
        else:
            X[i] = product(X[i],Q[i-2])
    return X[r]

n = 55
print(chain(n,7))





