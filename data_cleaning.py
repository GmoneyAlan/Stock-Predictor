import pandas as pd

df = pd.read_csv(r'C:\Users\alan2\Desktop\Projects\Stock-Predictor\Apple_stock_data.csv')

#Change date data format: Aug 14, 2020 -> 8/13/2020

df['Date'] = df['Date'].apply(lambda x: x.replace(' ', ''))
df['Date'] = df['Date'].apply(lambda x: x.replace(',','/'))

df['Date'] = df['Date'].apply(lambda x: x.replace('Jan', '1/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Feb', '2/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Mar', '3/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Apr', '4/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('May', '5/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Jun', '6/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Jul', '7/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Aug', '8/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Sep', '9/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Oct', '10/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Nov', '11/'))
df['Date'] = df['Date'].apply(lambda x: x.replace('Dec', '12/'))
   
#Change title
df.rename(columns={'Close*':'Close','Adj Close**':'Adj Close'},inplace=True)

#Make volume int
df['Volume'] = df['Volume'].apply(lambda x: x.replace(',',''))
df['Volume'] = df['Volume'].apply(lambda x: int(x))

df.to_csv(r'C:\Users\alan2\Desktop\Projects\Stock-Predictor\Apple_stock_data_cleaned.csv', index=False)
