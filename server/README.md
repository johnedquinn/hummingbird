PORT NUMBER: 75 

How our webserver can be used by a customer: 
Our WS will be used to access three things: Stock prices and information for specific stocks, top movers, which are stocks that have fluctuated the most in value over the last day, and charts, which will generate sequential data to produce a graph of the stock's price over a set period of time.

Our user will be able to see the stocks they have, the value of their stocks, and certain valuable information about the stock market and trends. 

Our resource specification strategy was based on the data that came from Yahoo Finance's RapidAPI as that response data was very structured. 

To run the tests for our WS, run our server with main.py so that we can get the necessary data through our yahoo finance API, then use `./test_ws.sh` to run the tests.

