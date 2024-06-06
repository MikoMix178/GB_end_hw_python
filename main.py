import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

new_data = pd.DataFrame()
for mean in data['whoAmI'].unique():
    new_data[f'{mean}'] = (data['whoAmI'] == mean).astype(int)

print(new_data.head())