# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:25:30 2018
Lecture 2 _code
@author: Administrator
"""
#for i in range(500):
#    print ("hello")

#my_list = [5,2,7,-4,0]
#for i in range (len(my_list)):
#    my_list [i] += 1
#print(my_list)

##############################
# loop until the user enters a positive number:
#num = float(input("Enter a positive number: "))
#while num <= 0.0:
#    num = float(input("Enter a POSITIVE nuber: "))
#    
## loop until the randomly generated number is greater than 0.5
#import random
#num = random.random()
#while num <= 0.5:
#    num = random.random()
#print(num)

#say you want to check whether any value in a list is great than 5
#my_list = [1,2,3,4,5,6,7,8]
#my_list2 = []
#greater_than_five = False
#
#for elem in my_list:
#    if elem >5:
#        greater_than_five = True
#        
#    if (greater_than_five):
#        my_list2.append(elem)
#print (my_list2)    

##################################
## EXAMPLE: perfect squares
##################################
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
    x = -x
while ans**2 < x:
    ans += 1
if ans**2 == x:
    if neg_flag:
        print(f"Square root of negative {-x} using imaginary number = {ans}i ")
    else:
        print("Square root of", x, "is", ans)
else:
    if neg_flag: 
        print(-x, "is not a perfect square")
    else:
        print(x, "is not a perfect square")

        
         