## program to generate simulated data for school childerns height and weight 

import numpy as np
import pandas as pd
import random

#random.seed(0)
count = 50
gender = np.random.binomial(1, 0.5, count) #male or female, 50% chance of either (We may need to modify this to express M/F/other(or did not disclose))
age = np.round(np.random.randint(13, 19, size=count))
height_factor = ((age*2)/30) #add variable to adjust height for age
weight_factor = ((age*2)/30) #add variable to adjust weight for age
school6 = np.column_stack((gender,age,))
df_base = pd.DataFrame(school6, columns=['gender','age']) #make df with headings

school6 = np.column_stack((gender,age,))
df_base = pd.DataFrame(school6, columns=['gender','age',]) #make df with headings
df_base.to_csv("school6.csv") #export the array to csv data frame with pandas

def weight_fn(row):   # row is a Series
    if row.gender == 1:
        return np.round(np.random.normal(70, 1.2),2)
    elif row.gender == 0:
        return np.round(np.random.normal(60, 1.2),2)
    else:
        return np.round(np.random.normal(65, 1.2),2)

def height_fn(row):   # https://www.skytowner.com/explore/creating_new_column_using_if_elif_and_else_in_pandas_dataframe
    if row.gender == 1:
        return np.round(np.random.normal((170), 1.2),2)
    elif row.gender == 0:
        return np.round(np.random.normal(160, 1.2),2)
    else:
        return np.round(np.random.normal(165, 1.2),2)

df_base["weight"] = df_base.apply(weight_fn, axis=1)*weight_factor
df_base["height"] = df_base.apply(height_fn, axis=1)*height_factor

df_base
print(df_base.head())
df_base.to_csv("school6.csv") #export the array to csv data frame with pandas



#df_base['sex'] = df_base['gender'].map({ 1 : 'male',0 : 'female'}) #df_base['Sex'] = df_base['Sex'].map({'male': 0,'female': 1})
#https://stackoverflow.com/questions/54052471/mapping-values-in-place-for-example-with-gender-from-string-to-int-in-pandas-d
