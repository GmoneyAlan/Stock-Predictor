import pandas as pd

df = pd.read_csv('Apple_stock_data')

#Change data
#Change title
#Make volume int
#salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
#minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
df['Volume']
print(df.isnull())
print(df.isna())
#df['Volume'] = df['Volume'].apply(lambda x: x.replace(',',''))


df.to_csv('Apple_stock_data_cleaned', index=False)
