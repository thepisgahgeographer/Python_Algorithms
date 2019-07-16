#!/usr/bin/env python
# coding: utf-8

# In[6]:


from arcgis.gis import GIS
gis = GIS()


# In[14]:


from IPython.display import display


# In[18]:


layer_results = gis.content.search('title: NC_Trout_Streams',
                                    'Feature Layer')


# In[19]:


NC_Trout_Streams = layer_results[0]

NC_Trout_Streams


# In[ ]:




