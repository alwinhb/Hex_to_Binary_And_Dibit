   
# Python code to convert HEX input to binary
# Further it will convert the binary to dibit code
# This dibit is useful for testing in DMR
#   -------------  
#   DEEPAK BAJAJ
#   -------------
import math 
from textwrap import wrap
from queue import Queue
import time
 

def Hex_To_Dibit() : 
    # Initialising hex string
    print ("\n")
    print("**************************************************************************************************")
    hex_string = input("Enter your hex value: \n")  
    print("Input Hex provided by you is :- \n ", hex_string)
    print("**************************************************************************************************")
    # Convert the hexadecimal string to binary using a list comprehension and string formatting  
    binary_string = ''.join(['{0:04b}'.format(int(d, 16)) for d in hex_string])  
    # Print the binary string  
    print("Resultant Binary Output is :- \n ", binary_string)  
    print("**************************************************************************************************")
    break_string = wrap(binary_string, width=2)
    Length = len(break_string)
    print("**************************************************************************************************")
    print("Breaking the resultant binary output to convert into dibit \n ",  break_string)
    print ("Length is \n", Length)
    print("**************************************************************************************************")
    print ("Dibit output is --> \n")
    dibit = ""
    final_output = ""
    for i in break_string:
        if i == "00" :
            dibit="0"
        elif i == "11" :
            dibit="3"
        elif i == "01" : 
            dibit="1"
        elif i == "10" :
            dibit="2"
        q = Queue()
        q.put(dibit)
        while not q.empty():
            print(q.get(), end='')

while True :
    Hex_To_Dibit()
    print ("\n")
    print ("-----------------------------------------------------------------------------------")
    print ("################################### DMR ###########################################")
    print ("-----------------------------------------------------------------------------------")
    print ("\n")
