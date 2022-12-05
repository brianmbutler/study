import requests
import os
from datetime import datetime, timedelta, date

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHAVANTAGE_KEY = os.environ.get('freestockapi')
NEWSAPI_KEY = os.environ.get('newsapi_key')


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'apikey': ALPHAVANTAGE_KEY
}


news_parameters = {
    'q': COMPANY_NAME,
    'apiKey': NEWSAPI_KEY
}

stock = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = stock.json()['Time Series (Daily)']

yesterday = date.today() - timedelta(days = 1)
print(yesterday)
day_before_yesterday = yesterday - timedelta(days = 1)

data_list = [value for key, value in data.items()]
yesterday = data_list[0]
yesterday_closing_price = float(yesterday['4. close'])
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday['4. close'])

price_change = abs(yesterday_closing_price - day_before_yesterday_closing_price)
percentage_difference_closing_price = (((yesterday_closing_price - day_before_yesterday_closing_price) / yesterday_closing_price) * 100)

news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data = news.json()['articles'][0:2]
headlines = [f"Headline: {article['title']}, \nBrief: {article['description']}" for article in news_data]
print(headlines)
# headlines = [value for key,value in articles['title']]
# print(headlines)

if percentage_difference_closing_price > 5:
    print("Get News")



#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

