import pandas as pd 

import green_noise

df = pd.read_csv("music_scales.csv")
#print(df)
data_top = df.head()    
# display  
print(data_top)# iterating the columns 

for col in df.columns: 
    print(col) 

green_noise.write_gn()
