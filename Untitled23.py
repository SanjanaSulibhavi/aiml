#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# In[13]:


# Sample Data
data = pd.read_csv('smart_grid_data.csv.csv')


# In[14]:


data


# In[15]:


# Display available column names
print("Available columns:", data.columns.tolist())


# In[16]:


data.columns = data.columns.str.strip()


# In[21]:


# Check if the required columns exist
required_columns = ['Temperature', 'Humidity', 'Hour of Day']
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    print(f"Missing columns: {missing_columns}")
else:
    # Proceed with selecting features and target
    X = data[required_columns]
    y = data['Energy_Consumption']


# In[23]:


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Verify the splits
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)



# In[19]:





# In[ ]:




