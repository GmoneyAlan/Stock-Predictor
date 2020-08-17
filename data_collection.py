import pandas as pd
import sys
sys.path.append(r'C:\Users\alan2\Desktop\Projects\Stock-Predictor')
from webscraper import get_stock_data

df = get_stock_data()

df.to_csv(r'C:\Users\alan2\Desktop\Projects\Stock-Predictor\Apple_stock_data',index=False)

