## program to generate simulated data for school childerns height and weight

import numpy as np
import pandas as pd
import random 
#random.seed(0)

weight_m = np.round(np.random.normal(65, 1.2, 50),2)
height_m = np.round(np.random.normal(1.7, 0.20, 50),2) #boys 170 and girls 160

weight_f = np.round(np.random.normal(55, 1, 50),2)
height_f = np.round(np.random.normal(1.6, 0.20, 50),2) #boys 170 and girls 160

school = np.column_stack((weight_m, height_m, weight_f, height_f))
df = pd.DataFrame(school, columns=['weight_m','height_m','weight_f','height_f']) #make df with headings
df.to_csv("school.csv") #export the array to csv data frame with pandas


mwm = np.round(np.median(school[:,0]),2) # median of weight_f
mhm = np.round(np.mean(school[:,1]),2) # mean of height_f
mwf = np.round(np.median(school[:,2]),2) # median of weight_m
mhf = np.round(np.mean(school[:,3]),2) # mean of height_m

print('Mean female height:')
print(mhf)
print('Mean male height:')
print(mhm)

print(df.describe())
