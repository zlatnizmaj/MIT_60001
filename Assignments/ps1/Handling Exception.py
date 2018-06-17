# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:44:51 2018

@author: Administrator
"""
# Handling Exception

#def inputNumber(message):
#  while True:
#    try:
#       userInput = int(input(message))       
#    except ValueError:
#       print("Not an integer! Try again.")
#       continue
#    else:
#       return userInput 
#       break 
#     
# 
##MAIN PROGRAM STARTS HERE:
#age = inputNumber("How old are you? ")
#
#if (age>=18):
#  print("You are old enough to vote.")
#else:
#  print("You will be able to vote in " + str(18-age) + " year(s).")
#################
def numInput(message):
	try:
		number = int(input(message))
	except:
		print ("You must enter a number")
		numInput()
	return number

def numInput2():
	number = input("Tell me a number: ")
	if number.isdigit():
		return number
	else:
		print ("You must enter a number (i.e. 0,1,2...)")
		numInput()

##################
def getNumberInRange(min, max):
    while 1:
        val = raw_input('Please enter a number between %s and %s' % (min, max) )
        try:
            val = int(val)
            if min <= val <= max:
                return val
        except ValueError:
            pass
        print 'Incorrect - please try again'