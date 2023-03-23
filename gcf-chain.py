# import addtion_chain as ac
import contfrac as cf

#TODO: make sure to choose a strategy later.
def minchain(n):
    l = n.bit_length() - 1 
    if n == 1<<l:
        return [2**(i) for i in range(l+1)]
    if n == 3:
        return [1,2,3]
    else:
        #line 7 from p.7, using square root method
        k = m.floor(m.sqrt(n))
        return chain(n,k)

def chain(n,k):
    u = cf.gcf(n,k)
    print("u: ",u)
    q0 = m.gcd(n,k)
    print("q0: ", q0)
    q1 = abs(u[0])*q0
    print("q1: ",q1)
    x0 = minchain(abs(q0))
    print("x0: ", x0)
    x1 = cf.product(x0,minchain(abs(u[0])))
    print("x1: ",x1)
    # return
    #should be a loop here but r =2
    # q2 = abs(u[1])*q1 +sign(u[0])*q0
    
    # print(res)
    x2 = cf.product(x1,minchain(abs(u[1])))
    print("x2: ", x2)
    
    if(u[0] < 0):
        x2 = cf.subtraction(x2,q0)
        print("x2: (subtraction) ", x2)
    else:
        x2 = cf.addition(x2,q0)
        print("x2: (addition)", x2)

    return (x2)

print(chain(55,7))





