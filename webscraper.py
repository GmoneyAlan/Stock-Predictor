import requests
from bs4 import BeautifulSoup as bs

'''
The stock we are scraping Apple
    we scraping data based on a daily basis
    from Yahoo Finance
    https://finance.yahoo.com/quote/AAPL/history?period1=790128000&period2=1597449600&interval=1d&filter=history&frequency=1d
'''
def get_stock_data():
    url = requests.get("https://finance.yahoo.com/quote/AAPL/history?period1=790128000&period2=1597449600&interval=1d&filter=history&frequency=1d")
    
    #Testing the page to make sure it is working 
    #print(url.status_code)
    #print(url.headers)
    
    #At the end of the data collection the list should contain data involving the day (Month/day/year)
        # As well as the closing price of the day
        # (n, $) where n is the day and $ is the closing price
        
    #Gets page content and stores it in index_html
    index_html = url.content
    
    soup = bs(index_html, 'lxml') 
    df = soup.find('tbody').find_all('span')
    
    title = ['Day', 'Close']
    
    #Day is in spot and close is in spot 5
    
    df_list = []
    count = 0
    
    for i in df:
        data = i.get_text()
        if data.isdigit():
            df_list.append(int(data))
        else:
            df_list.append(str(data))

    for i in df_list:
        print(i)
    print('Data printed')
    
if __name__ == "__main__":
    
    get_stock_data()