#!/usr/bin/env python
# coding: utf-8

# # The Weather Dataset.
# It is a time-series data set with per-hour information about the weather conditions at a particular location. It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure, and Conditions.
# I will analyze this data using Pandas DataFrame.

# In[2]:


import pandas as pd


# In[4]:


data = pd.read_csv(r'C:\Users\SPECTRE\Desktop\DataAnalysis_DataSets\Weather.csv.csv')


# In[5]:


data


# # ANALYZE DATAFRAME

# In[6]:


print(data.head()) #First n number of rows


# In[7]:


print(data.shape) #shows total no of rows and columns


# In[9]:


print(data.index) #provides the index of the dataframe


# In[10]:


print(data.columns) #shows name of each column


# In[14]:


data.dtypes     #shows data-type of each column


# In[15]:


print(data['Weather'].unique())  #apply on single column only, not on whole dataframe, shows unique values in each column


# In[16]:


data.nunique()   #shows total number of uniques values in each column


# In[17]:


data.count()   # shows total no. of non-null in each column


# In[19]:


data['Weather'].value_counts()  # for column only, shows all unique values with their counts


# In[20]:


data.info() #provides basic information about the dataFrame


# # Find all the unique 'Wind Speed' values in the data

# In[21]:


data.head(2)


# In[22]:


data.nunique()


# In[24]:


data['Wind Speed_km/h'].nunique()


# In[25]:


data['Wind Speed_km/h'].unique()


# # Find the number of times when the 'Weather is exactly Clear'

# In[29]:


data.head(2)


# In[30]:


#value_counts()
data.Weather.value_counts()


# In[32]:


#Filtering
data[data.Weather == "Clear"]


# In[33]:


#groupby
data.groupby('Weather').get_group('Clear')


# # Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[28]:


data.head(2)


# In[35]:


data[data['Wind Speed_km/h'] == 4]


# # Find out all the Null values in the data.

# In[36]:


data.isnull() #in boolean form


# In[38]:


data.isnull().sum()


# In[39]:


data.notnull().sum()


# In[ ]:





# # Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[40]:


data.head(2)


# In[43]:


data.rename(columns={"Weather":"Weather Condition"},inplace=True)


# In[44]:


data.head(2)


# # What is the mean 'Visibility'?

# In[45]:


data.head(2)


# In[47]:


data.Visibility_km.mean()


# # What is the Standard Deviation of 'Pressure' in this data?

# In[46]:


data.head(2)


# In[48]:


data.Press_kPa.std()


# # What is the Variance of 'Relative Humidity' in this data?

# In[49]:


data.head(2)


# In[50]:


data['Rel Hum_%'].var()


# # Find all instances when 'Snow' was recorded.

# In[51]:


data.head(2)


# In[53]:


# value_counts()
data['Weather Condition'].value_counts()


# In[54]:


# filtering
data[data['Weather Condition'] == "Snow"]


# In[57]:


# str.contains
data[data['Weather Condition'].str.contains('Snow')].tail(50)


# # Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'

# In[52]:


data.head(2)


# In[60]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# # What is the Mean value of each column against each 'Weaher Condition'

# In[64]:


data.head(2)


# In[66]:


data.groupby('Weather Condition').mean()


# # What is the Minimum & Maximum value of each column against each 'Weaher Condition'

# In[63]:


data.head(2)


# In[67]:


data.groupby('Weather Condition').min()


# In[68]:


data.groupby('Weather Condition').max()


# # Show all the Records where weather condition is Fog.

# In[62]:


data.head(2)


# In[69]:


data[data['Weather Condition']=='Fog']


# In[ ]:





# # Find all the instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[61]:


data.head(2)


# In[70]:


data[(data['Weather Condition']=="Clear") | (data['Visibility_km']>40)]


# In[ ]:





# # Find all instances when:
# # 'Weather is clear' and 'Relative Hmidity is greater than 50'
# 
# # or
# 
# # 'Visibility is above 40'

# In[71]:


data[(data['Weather Condition']=="Clear") & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)]


# In[ ]:




