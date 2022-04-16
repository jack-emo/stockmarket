# Stock Market Scraper
### Abstract
Built in Python3, this script scrapes stock ticker data using Alpha Vantage's API and displays it for the user to observe

### Built with
* [Pandas](https://pandas.pydata.org)
* [AlphaVantage](https://www.alphavantage.co)
* [Time](https://docs.python.org/3/library/time.html)

### Features
* Returns minute per minute ticker data for any given stock listed on any stock exchange 
* Able to send the data to a Microsoft Excel file for further analysis
* Prints an alert if the stock change was greater than a certain threshold (good for checking volatility)

### Usage
~/stockmarket python3 stocks.py

### Demo

Stock data for MSFT:

<img width="544" alt="Screen Shot 2022-04-16 at 4 28 03 PM" src="https://user-images.githubusercontent.com/77243976/163690402-27c49699-74b8-41dd-af74-7e8fef225f78.png">

Daily percentage change for MSFT:

<img width="257" alt="Screen Shot 2022-04-16 at 4 28 22 PM" src="https://user-images.githubusercontent.com/77243976/163690414-98baa7a8-62a5-42aa-8ef1-f00f8f0b91c9.png">
