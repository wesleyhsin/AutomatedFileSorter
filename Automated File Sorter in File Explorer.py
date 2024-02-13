#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Sort different types of files into their own folders using Python


# In[27]:


import os, shutil


# In[28]:


path = r"C:/Users/wesle/Documents/Python Tutorials/"
#r"" to make it a str


# In[29]:


file_name = os.listdir(path)


# In[30]:


folder_names = ['csv files', 'image files', 'text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))
        
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)


# In[26]:




