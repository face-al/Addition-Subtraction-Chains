# This is a setup to test my understanding

import addtion_chain as ac

if __name__ == "__main__":
    # z = 10

    # print("The NAF for", z, "is", ac.NAF(10))

    #test case for ac.product (XOR) refer to Doche p.196
    #Add more test cases with more random numbers and negative numbers.
    v = [10, 9, 7, 10, 5]
    w = [7, 4 , 8, 2, 5]
    result = ac.product(v,w)
    print("The XOR of v and w is %s" % result)
    
    print(ac.alpha(87)) 
    #test case for ac.addition (addition) refer to Doche p.196
    j = 10
    print(ac.addition(v,j))