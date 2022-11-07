## program to generate simulated data for school childerns height and weight

import numpy as np
import pandas as pd 

weight= np.random.normal(60, 15, 500)
height= np.random.normal(1.65, 0.20, 500) #boys 170 and girls 160

school2= np.column_stack((height, weight))

np.round(school2, decimals=2)
school2rounded = pd.DataFrame(school2).to_csv("school2.csv") #export the array to csv data frame with pandas
df = school2rounded

print(df)