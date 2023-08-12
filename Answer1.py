#!/usr/bin/env python
# coding: utf-8

# # Assignment-4: Map | Filter | Lambda
#     
# # Play with Lambda
# 
# # Q1. Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# In[3]:


value = float(input("Please give a number to add 25 to it: "))

r = lambda a : a + 25
print(r(value))

