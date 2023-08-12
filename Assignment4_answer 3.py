#!/usr/bin/env python
# coding: utf-8

# # Assignment-4: Map | Filter | Lambda
#     
# # Find the Squares from the given List
# 
# # Q3. Write a Python program to square the elements of a list using map() function.

# In[2]:


nums = eval(input("Enter a list of numbers to square: "))

def square_num(n):
  return n * n

print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))


# In[3]:


nums = eval(input("Enter a list of numbers to square: "))

print("Original List: ",nums)

result = map(lambda x: x*x, nums)

print("Square the elements of the said list using map():")
print(list(result))

