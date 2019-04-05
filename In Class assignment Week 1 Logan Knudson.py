# -*- coding: utf-8 -*-
"""
In class Problem set-Week 1
Annaconda 2, Python 2.7
"""

print("Eart119 -In Class Problem Set -Week I\nLogan Knudson")
###############################################################################
#   Problem 1

#============================================
#               Define Varriables
#============================================
n=10                    #Ammount of times to sum over 
Total=0                 #Total value of the sum 

#============================================
#               Calculation
#============================================
for i in range (1,n+1): #Summing 10 times
    Total += 5*i        #Sum calulation
print("-----------------------------------------\nProblem 1 Answer:\n Total Sum = %s"%(Total))

###############################################################################
#   Problem 2

#============================================
#               Importing Packages
#============================================

import numpy as np

#============================================
#               Define Varriables
#============================================
Piapprox=0                                   #the approximation of Pi
listN = [10,50,100,1000]                     #list of values of n 

#============================================
#               Calculation
#============================================
print("\n-----------------------------------------\nProblem 2 Answers:")
for N in listN:                              #looping over items in listN 
    Piapprox = 0                             #resets the approx of Pi from previous approximations
    for k in range (N+1):                    #Computing the Sum with N terms, were k is 0 through N
        Piapprox += 8./((4*k+1)*(4*k+3))     #Sum calculation
    print(" For N=%s"%(k))                   #printing Statements
    print(" Approximation of Pi = %s"%(Piapprox))
    print(" Error=%s\n" %(np.pi-Piapprox))

###############################################################################
#   Problem 3

#varriables a-g are strings containing the answers to parts in problem 3 (best read by running the code)
a = 'Python thinks this is a variable that has no assignment, therefore, the error code is telling you to give the variable "hello" a value, overall good error code.'         
b = 'Python thinks that this line is a for loop because of the statements "for" and "in" in the sentence. The sentence has invalid syntax if it was a for loop so python wants you to fix the syntax so it can run the line as a for loop. This is likely not the intended error code for a mistake like this.'
c = "This error is fairly clear, the statement is fairly meaningless and it tells you of the invalid syntax."
d = 'Error message and format is identical to part c, this time it was a spelling error in the word print. The invalid syntax message points towards y being the issue, this could be misleading.'
e = 'Changing the calculation of y does not produce an error code but it changes the value of y (incorrectly).'
f = "Changing y to x in the print statement tells python to print the value of the variable x but, x is not defined in the statements above therefore the error code tells you 'name 'x' is not defined' which is exactly what is happening."
g = 'Changing .5 to 1/2 changes the data type to an integer which is then rounded down to zero eliminating the rightmost term. No error code is displayed but this changes the value of y (incorrectly).'

print("-----------------------------------------\nProblem 3 Answers:\na.\n %s\n\nb.\n %s\n\nc.\n %s\n\nd.\n %s\n\ne.\n %s\n\nf.\n %s\n\ng.\n %s\n"%(a,b,c,d,e,f,g))










