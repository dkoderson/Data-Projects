#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn 


# # Load CSV file into memory
# 

# In[22]:


data = pandas.read_csv('Desktop/uber-raw-data-apr14.csv')


# In[21]:


data.tail()


# In[23]:


dt = '4/30/2014 23:22:00'


# In[29]:


dt = pandas.to_datetime(dt)


# In[40]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[35]:


data.tail()


# In[97]:


def get_dom(dt):
    return dt.day
 
data[ 'dom'] = data['Date/Time'].map(get_dom)

def get_weekday(dt):
    return dt.weekday()
 
data[ 'weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

data[ 'hour'] = data['Date/Time'].map(get_hour)


# In[98]:


data.tail()


# # analysis 

# 
# ## analyze the data form 

# In[113]:


hist(data.dom, bins=30,rwidth=.8, range= (0.5, 30.5))
xlabel('date of the month') 
ylabel('frequency') 
title('Frequency by DoM-uber-Apr2014') 


# In[128]:


for k, rows in data.groupby('dom'):
 print((k, rows))
 break 
    #print ((k,len(rows)))
    
def  count_rows(rows):
    return len(rows)
    
by_date = data.groupby('dom').apply(count_rows)
by_date


# In[131]:


bar(range(1,31),by_date)


# In[136]:


by_date_sorted = by_date.sort_values() 
by_date


# In[141]:


bar(range(1,31),by_date_sorted) 
xticks(range(1,31), by_date_sorted.index)
xlabel('date of the month') 
ylabel('frequency') 
title('Frequency by DoM-uber-Apr2014') 
("")


# ## analysis per hour

# In[145]:


hist(data.hour, bins=24 , range=(.5 , 24))  


# In[ ]:





# ### analyze the weekday 

# In[160]:


hist(data.hour, bins=7 , range=(-.5,6.5), rwidth=.8 , color='#AA6886' ,alpha=.4) 
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split()) 


# ###  cross analysis (hour, dow)

# In[168]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack() 


# In[171]:


seaborn.heatmap(by_cross)


# ### by latitude and longitude 

# In[180]:


hist(data['Lat'], bins=100, range = (40.5, 41)) 
("")


# In[194]:


hist(data['Lon'], bins=100, range = (-74.4,-73.58), color='g' , alpha=.5, label= 'longitude')
grid() 
legend(loc='upper left')
twiny()
hist(data['Lat'], bins=100, range = (40.5, 41), color ='r', alpha=.5, label= 'latitude')
legend(loc='best')
("")


# In[206]:


figure(figsize=(20,20)) 
grid()
plot(data['Lon'], data['Lat'],'.', ms=1, alpha =.5) 
xlim(-74.2, -73.7)
ylim(40.7,41)

