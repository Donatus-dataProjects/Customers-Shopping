#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_excel('Customer Call List.xlsx')
df.head(5)


# In[3]:


df = df.drop_duplicates()


# In[4]:


df


# In[5]:


df = df.drop(columns=['Not_Useful_Column'])


# In[6]:


df.head(5)


# In[7]:


#Removing symbols from values
df['Last_Name'] = df['Last_Name'].str.strip('123./_')
df['Last_Name']
df


# In[8]:


df['Phone_Number'] = df['Phone_Number'].str.strip('./_')
df['Phone_Number']
df


# In[9]:


#how to work on address (cleaning)
df[['Stress_Address', 'State', 'Zip_Code']] = df['Address'].str.split(',', n=2, expand=True)

df[['Stress_Address', 'State', 'Zip_Code']]


# In[10]:


df


# In[11]:


df.drop(columns = 'Zip_Code')


# In[12]:


df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')

df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')

df.head(5)


# In[13]:


df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')

df.head(5)


# In[14]:


df.head(5)


# In[15]:


df = df.drop(columns = ['Address'])
df.head(5)


# In[16]:


#replacing some values NaN
df = df.fillna('')
df


# In[17]:


df


# In[18]:


df.replace('', np.nan, inplace=True)


# In[19]:


df


# In[46]:


df.replace('N/a', np.nan, inplace=True)
df


# In[47]:


df


# In[48]:


df


# In[23]:


df['Paying Customer'] = df['Paying Customer'].str.replace('N/a', 'NaN')


# In[24]:


df['Stress_Address'] = df['Stress_Address'].str.replace('N/a', 'NaN')


# In[49]:


df


# In[50]:


df['Paying Customer'].value_counts()


# In[51]:


df['Do_Not_Contact'].value_counts(dropna=False)


# In[52]:


df['Phone_Number'].value_counts(dropna=False)


# In[53]:


nan_count = df['Phone_Number'].isna().sum()
print("NaN", nan_count)


# In[54]:


# Data
categories = ['Y', 'N', 'Not Available']
values = [13, 6, 1]

# Plot
sns.barplot(x=categories, y=values)
# Add annotations
for index, value in enumerate(values):
    plt.text(index, value + 0.2, str(value), ha='center', va='bottom')

# Add title and labels
plt.title('Paying Customers')
plt.xlabel('Customer Status')
plt.ylabel('Number of Customers')

# Show plot
plt.show()


# In[55]:


# Data
categories = ['Y', 'N', 'Not Available']
values = [12, 4, 4]

# Plot
sns.barplot(x=categories, y=values )
# Add annotations
for index, value in enumerate(values):
    plt.text(index, value + 0.2, str(value), ha='center', va='bottom')

# Add title and labels
plt.title('Do Not Contact')
plt.xlabel('Customer Status')
plt.ylabel('Number of Customers')

# Show plot
plt.show()


# In[56]:


fig, axes = plt.subplots(1, 2, figsize = (14, 6))

#First plot
categories1 = ['Y', 'N', 'Not Available']
values1 = [12, 4, 4]

#Second plot
categories2 = ['Y', 'N', 'Not Available']
values2 = [13, 6, 1]

sns.barplot(x=categories1, y=values1, ax=axes[0])

#Annotations
for index, value in enumerate(values1):
    axes[0].text(index, value + 0.2, str(value), ha='center', va='bottom')
    
axes[0].set_title('Do Not Contact')
axes[0].set_xlabel('Customer Status')
axes[0].set_ylim(0, 20)


sns.barplot(x=categories2, y=values2, ax=axes[1])
# Annotations
for index, value in enumerate(values2):
    axes[1].text(index, value + 0.2, str(value), ha='center', va='bottom')

axes[1].set_title('Paying Customers')
axes[1].set_xlabel('Customer Status')
axes[1].set_ylim(0, 20)

plt.tight_layout()


# In[ ]:




