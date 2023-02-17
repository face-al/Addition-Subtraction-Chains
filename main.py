# This is a setup to test my understanding

import addtion_chain as ac
import numpy as np

if __name__ == "__main__":
    # z = 10

    # print("The NAF for", z, "is", ac.NAF(10))

    #test case for ac.product (XOR) refer to Doche p.196
    #Add more test cases with more random numbers and negative numbers.
    v = [10, 9, 7, 10, 5]
    w = [7, 4 , 8, 2, 5]
    result = ac.product(v,w)
    assert(w,v)
    
    #test case for ac.addition (addition) refer to Doche p.196
    j = 10
    print(ac.addition(v,j))
   
    
    # #Case when n == 2**l, so n = 256, should return [1,...,2**l]
    n, alpha = 29, ac.alpha(256)
    print("n is %d and alpha is %d" % (n,alpha))
    print(ac.chain(n,alpha))
    
    print(len([1, 2, 4, 8, 10, 11, 18, 36, 47, 55, 91, 109, 117, 226, 343, 434, 489, 499, 933, 1422, 2844, 5688, 5689]))
    a = 26235947428953663183191
    print(a.bit_length())
    #test with numpy
    # v = [4,3,2,5]
    # w = [4,8,1]
    # print(np.multiply(v[-1],w))
    
    
    #debugging product and addition
    # print(ac.addition(ac.product([1,2,3],[1,2]),1))
