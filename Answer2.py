#!/usr/bin/env python
# coding: utf-8

# # Assignment-4: Map | Filter | Lambda
#     
# # Find the way with Maps
# 
# # Q2. Write a Python program to triple all numbers of a given list of integers. Use Python map.

# In[5]:


num = eval(input("Please enter numbers to tripple :  "))

result = map(lambda x: x + x + x, num) 
print("\nTriple of said list numbers:")
print(list(result))


# In[4]:


num = eval(input("Please enter numbers to tripple :  "))

def tripple(num):
    num = num+num+num
    return num

result = map(tripple, num)
print("\nTriple of said list numbers:")
print(list(result))


# In[ ]:




