
# coding: utf-8

# In[1]:

get_ipython().system('pip install monkeylearn')


# In[2]:

from monkeylearn import MonkeyLearn


# In[23]:

ml = MonkeyLearn('f99795609070a09a162a53d6ffbfcc91032b5879')
data = [input("Enter Text here to check : ")]
model_id = 'cl_HNNqWdyi'
result = ml.classifiers.classify(model_id, data)
file=result.body
print("Result : "+file[0]['classifications'][0]['tag_name'])


# In[24]:

ml = MonkeyLearn('f99795609070a09a162a53d6ffbfcc91032b5879')
data = [input("Enter Text here to check : ")]
model_id = 'cl_HNNqWdyi'
result = ml.classifiers.classify(model_id, data)
file=result.body
print("Result : "+file[0]['classifications'][0]['tag_name'])


# In[ ]:



