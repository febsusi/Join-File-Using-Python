#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


xls = pd.ExcelFile("C:/Users/Asus/Documents/Book1.xlsx")

traindff = xls.parse(0) #2 is the sheet number


# In[3]:


traindff.info()


# In[6]:


dff = traindff.applymap(str)


# In[ ]:


dff = traindff.applymap(str)


# In[ ]:


df['Zip_Code']=df['Zip_Code'].apply(lambda x: '{0:0>5}'.format(x))


# In[7]:


dff.info()


# In[4]:


xlb = pd.ExcelFile("C:/Users/Asus/Documents/Book1.xlsx")

traindf = xls.parse(1) #2 is the sheet number


# In[5]:


traindf.info()


# In[18]:


xlc = pd.ExcelFile("D:/Regsosek/Unique/kodeunik5.xlsx")

traindfd = xlc.parse(0) #2 is the sheet number


# In[6]:


inner_join = pd.merge(traindff,
                      traindf,
                     on = 'Nama',
                      how = 'inner')
inner_join


# In[18]:


pd.merge(traindff,traindf,on='Nama')


# In[ ]:


results=filtered_df.merge(csv, on = 'Nama')


# In[ ]:


display (results)


# In[ ]:


results.to_excel (r'C:/Users/Asus/Downloads/book122coba.xlsx', index = False, header = True)


# In[ ]:


jatiasih = pd.ExcelFile("D:/Regsosek/Data Mentah/jatiasihaj.xlsx")

jat = xls.parse(0) #2 is the sheet number


# In[10]:


agg_df = kay.groupby(by = 'Nama').agg(count=('Nama','count'))
agg_df.reset_index(inplace=True)


# In[ ]:


unique_df=agg_df.loc[agg_df['count']>1].merge(dff, on =['Nama'])


# In[ ]:


unique_df.to_excel (r'C:/Users/Asus/Downloads/book11cobaunique.xlsx', index = False, header = True)


# In[15]:


kayu = pd.ExcelFile("D:/Regsosek/Data Mentah/pplkayuringin2.xlsx")

kay = xls.parse(0)


# In[17]:


kay.info()


# In[11]:


filtered_df=agg_df.loc[agg_df['count']==1].merge(kay, on =['Nama'])


# In[12]:


filtered_df.to_excel (r'D:/Regsosek/Unique/kayunik.xlsx', index = False, header = True)


# In[ ]:


filter_df = pd.ExcelFile("D:/Regsosek/Unique/unikbanget.xlsx")

filterr = xls.parse(0) #2 is the sheet number


# In[18]:


filterr.head(20)


# In[23]:


duplicate = jat[jat['NIK'].duplicated(keep=False)]
print("Duplicates:", duplicate)


# In[15]:


noduplicate.to_excel (r'C:/Users/Asus/Downloads/bookduplicate.xlsx', index = False, header = True)


# In[24]:


duplicate.to_excel (r'C:/Users/Asus/Downloads/toko.xlsx', index = False, header = True)


# In[7]:


inner_join.to_excel (r'D:/Regsosek/Data Mentah/pplkayuringin.xlsx', index = False, header = True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




