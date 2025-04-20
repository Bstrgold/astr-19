#!/usr/bin/env python
# coding: utf-8

# # Sine and Cosine Function Tabulation
# 
# In this notebook, we define and use functions for `sin(x)` and `cos(x)`, tabulate them over the interval `[0, 2]` with 1000 entries, and display the first 10 results.

# ### sin_function(x)
# 
# This function takes a value `x` as input and returns `sin(x)` using Python's built-in `math.sin()` function.

# In[1]:


import math

def sin_function(x):
    """
    Returns the sine of x.
    """
    return math.sin(x)


# ### cos_function(x)
# 
# This function takes a value `x` as input and returns `cos(x)` using Python's built-in `math.cos()` function.

# In[2]:


def cos_function(x):
    """
    Returns the cosine of x.
    """
    return math.cos(x)


# ### Tabulate sin(x) and cos(x) 
# 
# using these previously defined functions vs. x, where x is tabulated between 0 and 2 with a thousand entries

# In[3]:


num_points = 1000
start = 0
end = 2
step = (end - start) / (num_points - 1)

x_values = [start + i * step for i in range(num_points)]
sin_values = [sin_function(x) for x in x_values]
cos_values = [cos_function(x) for x in x_values]


# ### Print First 10 Values
# 
# Use a loop to print the first 10 values of `x`, `sin(x)`, and `cos(x)` side by side in column format.

# In[4]:


print(f"{'x':>10} {'sin(x)':>15} {'cos(x)':>15}")
print("-" * 40)
for i in range(10):
    print(f"{x_values[i]:10.6f} {sin_values[i]:15.6f} {cos_values[i]:15.6f}")


# In[ ]:




