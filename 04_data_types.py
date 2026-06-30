#data types is something that is used to define the type of data that we are storing in a variable. python has different types of data types like numbers, strings, lists, tuples, dictionaries, etc.

#data types are of 3 types -
"""1. Numbers
2. Strings
3. Boolean"""
 
# 1. Numbers
 # Integer- all the numbers excluding decimal points are called integers. for example, 1,2,3,4,5,6,7,8,9,10 are all integers.
 # Float- all the numbers including decimal points are called floats. for example, 1.1, 2.2, 3.3, 4.4, 5.5 are all floats.
 # complex- all the numbers including imaginary numbers are called complex numbers. for example, 1+2j, 2+3j, 3+4j are all complex numbers.

import code
from os import name


a = 69      #integer example

print(type(a))

b = 69.69   #float example

print(type(b))

c = 1+2j    #complex example

print(type(c))



"""Strings"""
# this is used to store anything in python. we can store anything in strings like numbers, letters, special characters, etc. we can use single quotes, double quotes and triple quotes to store data in strings.


st="hello world"

print(type(st))
    
"""Boolean"""
 
 # this is used to store True or False values in python. we can use boolean values to check if a condition is true or false.
 # for example 

S=True

A=False

print(type(S))
print(type(A))



"""Strings and type conversions"""

#String take more space than other data types like int float etc

# this happens because string stores every character with thier own unicode

#unicode is a universal character encoding standard that assigns a unique number to every character in every language in the world. this is done to ensure that every character is represented in a unique way and can be used in any language.


# code example below;

A = "A"

print(ord(A)) 

#output- 65

"""NOTE"""
   # ord() function se sirf ek character ka unicode milta hai. agar aapko ek string ka unicode chahiye to aapko har character ka unicode alag alag lena padega. 

Sujal = "8"

print(ord(Sujal))


# now if we want to get unicode of a word or a sentence then we can use char() function to get the unicode of a word or a sentence. char() function takes an integer as an argument and returns the character that corresponds to that integer in the unicode table..
# for example, if we want to get the unicode of the word "hello" then we can use char() function to get the unicode of each character in the word "hello" and then we can concatenate them to get the unicode of the word "hello".  


name = "Sujal"
for ch in name:
    print(ch,ord(ch))

#output-
# S 83
# u 117
# j 106
# a 97
# l 108


# ORD converts a character to its unicode value and CHR converts a unicode value to its character.



"""String indexing"""



a = "Sujal Gupta"
print(a[3])


#output- a

# this is known as string indexing.
# we can access it by its index number.
# its starts fron 0 and goes upto n-1 where n is the length of the string.


#example -
S = "Sujal Gupta"
print(S[6], S[-4])

#output - G u 


text = "Sujal Gupta"
print(text[0:7])

#output- Sujal G

text = "i am learning python programming"
print(text[0:12])

#output- i am learning

text = "i am new to in this world of programming"
print(text[0:18])
#output- i am new to in this


text = "hey what are you doing?"
print(text[0:3])
#output- hey


text = "hey what are you doing?"
print(text[0:3:1])

text = "hey how are you doing?"
print(text[0:3:3])


a = "Sujal Kumar Gupta"
print(a[0:5])



