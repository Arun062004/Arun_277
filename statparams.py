#!/usr/bin/env python
# coding: utf-8

# In[13]:


def mean_value(given_list):
    total= sum(given_list)
    average_value = total/len(given_list)
    return average_value
L=[10,11,12,11,22,33]
mean_value(L)


# In[55]:


def mode_value(s):
    s = set(L)
    d ={}
    for x in s:
        d[x]= L.count(x)
    m = max(d.values())

    for k in d.keys():
        if d[k] == m:
            return k
L = ["s","s","s","a","a"]
mode_value(L)
    
    


# In[57]:


L =[2,22,3,3,3]
mode_value(L)


# In[ ]:




