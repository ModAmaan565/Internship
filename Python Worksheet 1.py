#!/usr/bin/env python
# coding: utf-8

# In[5]:


Ans1:-C) %
Ans2:- B) 0
Ans3:- C) 24
Ans4:- A) 2
Ans5:- D) 6
Ans6:- C) The finally block will be executed no matter if the try block raises an error or not.
Ans7:- A) It is used to raise an exception.
Ans8:- C) In defining a generator
Ans9:-
A) _abc
C) abc2
Ans10:-  
     A) yield
     B) raise


# In[ ]:


# Ans 11:-

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *=i
    
print("the factorial of", num)


# In[ ]:


number = int(input("Enter a number: "))

result = 1

i = 1
while i <= number:
    result *= i
    i += 1

# Print the result
print(f"The factorial of {number} is: {result}")


# In[ ]:


# Ans12. 

num = int(input("Enter a number: "))

if num <= 1:
    print(f"The number {num} is neither prime nor composite.")
else:
    is_prime = True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"The number {num} is Prime.")
    else:
        print(f"The number {num} is Composite.")


# In[ ]:


# Ans13.

string = input("Enter a string: ")

s = string.lower().replace(" ", "")

if s == s[::-1]:
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")


# In[ ]:


# Ans14.

import math

a = float(input("Enter the length of the first side (a): "))
b = float(input("Enter the length of the second side (b): "))

c = math.sqrt(a**2 + b**2)

print(f"The length of the hypotenuse (third side) is: {c}")


# In[ ]:


# Ans15.


string = input("Enter a string: ")

frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequencies:")
for char in frequency:
    print(f"{char}: {frequency[char]}")


# In[ ]:




