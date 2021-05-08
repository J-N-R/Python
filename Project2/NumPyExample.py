# Mini Project to play around with the power of NumPy!
#
# Description:
#    NumPy is an amazing tool to solve grand, data based problems, that can bring a lot of power and speed to your programs!
#
#    While I would've loved to tie this together with panda dataframes, due to time constraints,
#    I made this simple project that allows a user to create a NumPy array, and perform an operation on all elements.
# 
import numpy


print("Welcome to my NumPy Calculator!")
print("Give me a list of numbers, and I'll be able to do an operation to every element in that list.")


myinput = input("Give me a number, or a list of numbers.  [Example: '5' or '7 8 15 13']\n\n")


inputList = myinput.split(" ")
numpyArray = []


try:
    for i in range( len(inputList) ):
        numpyArray.append( float(inputList[i]) )


    numpyArray = numpy.array( numpyArray )
    
    print("Your Array is: ", numpyArray)
    operator = str(input("\nPlease input what operator you would like to use: +, -, /, *, **\n"))
    
    print("\nPlease input your operand.\n", numpyArray, " ", operator, " ", end="")
    operand = float(input())
    
    if operator == '*':
        print("\nYour new Array: ", numpyArray * operand)
    elif operator == '+':
        print("\nYour new Array: ", numpyArray + operand)
    elif operator == '-':
        print("\nYour new Array: ", numpyArray - operand)
    elif operator == '/' and operand == 0:
        print("Division by Zero Error. Please try again.")
    elif operator == '/':
        print("\nYour new Array: ", numpyArray / operand)
    elif operator == '**':
        print("\nYour new Array: ", numpyArray ** operand)
    else:
        print("\nUnknown Operator. Please only use the listed operators, and try again.")
    
except:
    print("\nError when making your list. Please make sure you only put numbers and spaces."
