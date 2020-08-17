from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

'''
The stock we are scraping Apple
    we scraping data based on a daily basis
    from Yahoo Finance
    https://finance.yahoo.com/quote/AAPL/history?period1=790128000&period2=1597449600&interval=1d&filter=history&frequency=1d
'''
def get_stock_data():
    #url that we are scraping
    url = "https://finance.yahoo.com/quote/AAPL/history?period1=790128000&period2=1597449600&interval=1d&filter=history&frequency=1d"

    #Selenium opens scroll on 'url' and scrolls all the way down 
    driver = webdriver.Chrome(r'C:\Users\alan2\Desktop\Projects\Stock-Predictor/chromedriver.exe')
    driver.get(url)
    
    #Testing the page to make sure it is working 
    #print(url.status_code)
    #print(url.headers)
    
    #loop that scrolls till it reaches the bottom of the page
    for i in range(70):
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(1)
    
    #At the end of the data collection the list should contain data involving the day (Month/day/year)
        # As well as the closing price of the day
        # (n, $) where n is the day and $ is the closing price
        
    #Gets page content and stores it in index_html
    index_html = driver.page_source
    
    driver.close()
    
    soup = bs(index_html, 'html.parser') 
    data_html = soup.find('tbody').find_all('span')
    title_html = soup.find('thead').find_all('span')
    
    title_list = []
    for i in title_html:
        title_list.append(i.get_text())
    
    data_list,data_set = [], []
    MAX = len(title_list) 
    
    for i in data_html:
        data = i.get_text()
        if data.isdigit():
            data_set.append(int(data))
        else:
            data_set.append(str(data))
        if MAX == len(data_set):
            data_set = []
            data_list.append(data_set)

    df = pd.DataFrame(data_list,columns=title_list)
    
    return df