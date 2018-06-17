# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:42:11 2018
Lecture 3_MIT60001
@author: Administrator
"""
s = "hello"
#s[0] = 'y'
s = 'y' + s[1:len(s)]
print(s)

s1 ="abcdefgh"
print(s1[3:6])
print(s1[::])
print(s1[0:len(s): 1])
print(s1[::-1])

# for index in range(len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#         print("There is an i or u")

for char in s:
    print(char)
    if char =='i' or char == 'u':
        print ("There is an i or u")

######################
## ROBOT CHEERLEADERS
######################
an_letters = 'aefhilmnorsxAEFHILMNORSX'
word = input("I will cheer for you ! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

#i = 0
#while i < len(word):
    # char = word[i]
for char in word:
    print(char)
    found = False
    if char in an_letters:
        found = True
        print(found)
        print("Give me an: " + char + "! " + char)
    else:
        print(found)
        print("Give me a: " + char + "! " + char)
    # i += 1
print("What does that spell")
for i in range(times):
    print(word, "!!!")
##########################
