#First I would need to code a dictionary
#then I would need to apply Bos-Coster \
#test example would be n = 5689
# This example is only for signed integer only 
#if integer uis unsigned, then there has to slight modification
import numpy as np

def NAF(x):
    if x == 0:
        return []
    z = 0 if x % 2 == 0 else 2 - (x % 4)
    return NAF( (x-z) // 2 ) + [z]

#write an NAF_inverse function


n = 587257

n_naf = NAF(n)
zeros_in_n = n_naf.count(0) #count number of zeros
l = len(n_naf)

#p = # of 0's/ length of n (bit length)
p = zeros_in_n/l

#q_hat because we are dealing with NAF (signed integer)
q_1 = round((1-p)/2,2)

# k = 4, just as in 9.35 from Doche and leaves are initially 1, it is just the root initially
leaves = 0
k = 4
# w = 1 #weight of root node
# res = [1]
# weight = [0, -10, 10]
# weight_prob = {p: weight[0], q_hat: weight[1]}
#we start with root and its weight is one
tree = {"root": 1}
signed_appending = {p:0, q_1: [-10,10]}
tree.update(signed_appending)
print(tree)
# while(leaves < k+1):
#     # we have three labels [0, -10, 10], because it is signed
