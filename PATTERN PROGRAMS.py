#!/usr/bin/env python
# coding: utf-8

# In[11]:


#1 Right angled triangle 
n=int(input())
for i in range(1,n+1): 
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[13]:


#2-->Right angled triangle with odd positions 
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1): 
        if i%2!=0: 
            print("*",end=" ")
    print()


# In[17]:


#2-->Printing the odd numbers in the pattern 
n=int(input())
k=1 
for i in range(1,n+1): 
    for j in range(1,k+1): 
        print("*",end=" ")
    k=k+2 
    print()


# In[1]:


#3----->PYRAMID PATTERN 
n=int(input())
for i in range(n+1): 
    for j in range(n-i+1): 
        print(end=" ")
    for j in range(i): 
        print("*",end=" ")
    print()


# In[4]:


#4--->PYRAMID PATTERN PROGRAM 
n=int(input())
for i in range(n+1): 
    for j in range(n-i+1): 
        print(" ",end=" ")
    for j in range(0,2*i+1): 
        print("*",end=" ")
    print()


# In[43]:


#5--->REVERSE PYRAMID 
n=int(input())
for i in range(n,0,-1): 
    for j in range(n-i): 
        print(end=" ")
    for j in range(i): 
        print("*",end=" ")
    print()


# In[50]:


#5---> REVERSE OF THE PROGRAM 
n=int(input())
for i in range(1,n+1): 
    for j in range(1,i+1): 
        print(" ",end=" ")
    for j in range(n-i): 
        print("*",end=" ")
    for j in range(n-i+1): 
        print("*",end=" ")
    print()


# In[53]:


#5--->REVERSE PYRAMID 
n=int(input())
for i in range(n,0,-1): 
    for j in range(3*n-i): 
        print(end=" ")
    for j in range(i): 
        print("*",end=" ")
    print()


# In[7]:


def find_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# Reading input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calling the function and printing the result
gcd = find_gcd(a, b)
print("GCD:", gcd)


# In[5]:


import math 
a=math.gcd(20,50)
print(a)


# In[9]:


import math 
a=math.gcd(10,20,30)
print(a)


# In[62]:


n=int(input())
for i in range(n,0,-1): 
    for j in range(n-i+1): 
        print(end=" ")
    for j in range(i): 
        print("*",end=" ")
    print()


# In[104]:


#Diamond 
n=int(input())
for i in range(n): 
    for j in range(n-i): 
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n,0,-1): 
    for j in range(n-i): 
        print(end=" ")
    for j in range(i): 
        print("*",end=" ")
    print()


# In[111]:


#DECREMENT TRIANGLE 
n=int(input())
for i in range(1,n+1): 
    for j in range(n-i+1): 
        print("*",end=" ")
    print()


# In[114]:


#decrement Triangle 
n=int(input())
for i in range(n,0,-1): 
    for j in range(i): 
        print("*",end=" ")
    print()


# In[122]:


#alphabetical order: 
for r in range(7): 
    for c in range(5): 
        if ((c==0 or c==4) and r!=0) or ((r==0 or r==3) and (c>0 and c<4)): 
            print("*",end=" ")
        else: 
            print(end="  ")
    print()


# In[149]:


for r in range(7): 
    for c in range(5): 
        if ((c==0 or c==4) or (r>0 and r<4)): 
            print("*",end=" ")
    print()


# In[166]:


for r in range(7): 
    for c in range(5): 
        if ((c==0 or c==4) or (r==0 or r==6) or (r==3)):
            print("*",end=" ")
        else: 
            print(end="  ")
    print()


# In[168]:


for r in range(7): 
    for c in range(5): 
        if (((c==0 or c==4) or (r==0 or r==6) or (r==3)) or (c>0 and c<4)):
            print("*",end=" ")
        else: 
            print(end="  ")
    print()


# In[179]:


for r in range(7): 
    for c in range(5): 
        if ((c==0 or c==4)) or (r==0 or r==3 or r==6): 
            print("*",end=" ")
        else: 
            print(end="  ")
    print()


# In[10]:


n=int(input())
for i in range(n): 
    for j in range(n): 
        if i==0 or i==n-1 or j==0 or j==n-1: 
            print("*",end=" ")
        else: 
            print(end="  ")
    print()


# In[14]:


n=int(input())
for i in range(n): 
    for j in range(n): 
        if i==0 or i==n-1 or j==0 or j==n-1: 
            print("*",end=" ")
        else: 
            print(end="  ")
    print()


# In[17]:


for r in range(4):
    for c in range(4): 
        if r==0 or r==3 or c==0 or c==3 or r==2:
            print("*",end=" ") 
        else: 
            print(end="  ")
    print()


# In[21]:


n=int(input())
for i in range(1,n+1): 
    for j in range(1,i+1): 
        print(j,end=" ")
    print()


# In[27]:


n=int(input())
for i in range(1,n+1): 
    for j in range(i,0,-1): 
        print(j,end=" ")
    print()


# In[30]:


n=int(input())
for i in range(1,n+1): 
    for j in range(1,i+1): 
        print(i,end=" ")
    print()


# In[35]:


n=int(input())
for i in range(1,n+1): 
    for j in range(1,i+1): 
        print(n-i+1,end=" ")
    print()


# In[ ]:




