# import addtion_chain as ac
import contfrac as cf
import math as m

#TODO: make sure to choose a strategy later.

# Reference:
# 1: Binary Strategy
# 2: Modified-Binary Strategy
# 3: Factor Strategy
# 4: Pi Strategy
# 5: Golden-Ratio Strategy
# 6: Square-root Strategy
# 7: Seventh Strategy
# 8: Ones strategy 


def minchain(n, strategy_num):
    l = n.bit_length() - 1 
    strategy = {1: cf.floor(n/2), 2: cf.floor(m.sqrt(n))}
    if n == 1<<l:
        return [2**(i) for i in range(l+1)]
    if n == 3:
        return [1,2,3]
    else:
        #line 7 from p.7, using square root method
        k = strategy[strategy_num]
        return chain(n,k, strategy_num)

def chain(n,k, strategy_num):
    u = cf.gcf(n,k)
    #Check if u1 and u2 is not 0 
    if u[0] == 0 or u[1] == 0:
        return cf.chain(n,k)
    # print("u: ",u)
    q0 = m.gcd(n,k)
    # print("q0: ", q0)
    q1 = abs(u[0])*q0
    # print("q1: ",q1)
    x0 = minchain(abs(q0), strategy_num)
    # print("x0: ", x0)
    x1 = cf.product(x0,minchain(abs(u[0]),strategy_num))
    # print("x1: ",x1)
    
    # return
    #should be a loop here but r =2
    # q2 = abs(u[1])*q1 +sign(u[0])*q0
    # print(res)
    
    x2 = cf.product(x1,minchain(abs(u[1]), strategy_num))
    # print("x2: ", x2)
    if(u[0] < 0):
        x2 = cf.subtraction(x2,q0)
        # print("x2: (subtraction) ", x2)
    else:
        x2 = cf.addition(x2,q0)
        # print("x2: (addition)", x2)
    
    return sorted(list(set(x2)))


k = 3
# for i in range(6,100):
#     print("for i = ",i,chain(i,k,2))
print(chain(63,7,1))





