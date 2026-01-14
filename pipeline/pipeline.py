import sys
import pandas as pd
month=int(sys.argv[1])


df=pd.DataFrame({"day":[1,2], "num_passangers":[5,6]})
df['month']=month
print(df.head())
print(f'hello pipeline month= {month}')

df.to_parquet(f"output_{month}.parquet")