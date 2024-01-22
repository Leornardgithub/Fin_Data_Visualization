"""Module for streamig live data from tws"""
"""
A class that inherits from EClient and EWrapper to handle 
live data streaming.
"""
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Thread

class LiveDataManager(EWrapper, EClient):
    
    """Serves as the client and the wrapper"""
    """
    Ib live data methods:
        -reqMktData: Request market data
            -cancelMktData: Cancel market data
            
        -reqMktDepth: Request market depth
            -cancelMktDepth: Cancel market depth
            
        -reqRealTimeBars: Request real-time bars
            -cancelRealTimeBars: Cancel real-time bars
            
        -reqTickByTickData: Request tick-by-tick data
            -cancelTickByTickData: Cancel tick-by-tick data
    """
    
    def __init__(self):
        EClient.__init__(self, self)
        
    def request_candlestick_data(self):
        # Prompt for user input
        symbol = input("Enter the symbol (e.g., AAPL): ")
        secType = input("Enter the security type (e.g., STK for stock): ")
        exchange = input("Enter the exchange (e.g., SMART): ")
        currency = input("Enter the currency (e.g., USD): ")

        # Create a contract object and define its parameters
        contract = Contract()
        contract.symbol = symbol
        contract.secType = secType
        contract.exchange = exchange
        contract.currency = currency

        # Request real-time bars
        self.reqRealTimeBars(1, contract, 5, "MIDPOINT", True, [])
        
    def request_tick_by_tick_data(self, symbol, secType, exchange, currency):
        # Prompt for user input
        symbol = input("Enter the symbol (e.g., AAPL): ")
        secType = input("Enter the security type (e.g., STK for stock): ")
        exchange = input("Enter the exchange (e.g., SMART): ")
        currency = input("Enter the currency (e.g., USD): ")

        # Create a contract object and define its parameters
        contract = Contract()
        contract.symbol = symbol
        contract.secType = secType
        contract.exchange = exchange
        contract.currency = currency

        # Request tick-by-tick data
        # The 'Last' type provides the last trade's price and size
        self.reqTickByTickData(1, contract, "Last", 0, False)

        # You can request additional types of tick-by-tick data as needed
        # For example, 'BidAsk' provides bid and ask price and size
        # self.reqTickByTickData(2, contract, "BidAsk", 0, False)

    def request_time_and_sales_data(self):
        # Prompt for user input
        symbol = input("Enter the symbol (e.g., AAPL): ")
        secType = input("Enter the security type (e.g., STK for stock): ")
        exchange = input("Enter the exchange (e.g., SMART): ")
        currency = input("Enter the currency (e.g., USD): ")

        # Create a contract object and define its parameters
        contract = Contract()
        contract.symbol = symbol
        contract.secType = secType
        contract.exchange = exchange
        contract.currency = currency

        # Request tick-by-tick data for time and sales
        self.reqTickByTickData(1, contract, "Last", 0, False)

        # Note: Depending on the details you need, you might use other tick types
        # For instance, "AllLast" can be used to include OTC trades

    def request_market_depth(self, symbol, secType, exchange, currency):
        # Prompt for user input
        symbol = input("Enter the symbol (e.g., AAPL): ")
        secType = input("Enter the security type (e.g., STK for stock): ")
        exchange = input("Enter the exchange (e.g., SMART): ")
        currency = input("Enter the currency (e.g., USD): ")

        # Create a contract object and define its parameters
        contract = Contract()
        contract.symbol = symbol
        contract.secType = secType
        contract.exchange = exchange
        contract.currency = currency

        # Request real-time bars
        self.reqRealTimeBars(1, contract, 5, "MIDPOINT", True, [])
    
    def request_real_time_volume_bar_data(self):
        # Prompt for user input
        symbol = input("Enter the symbol (e.g., AAPL): ")
        secType = input("Enter the security type (e.g., STK for stock): ")
        exchange = input("Enter the exchange (e.g., SMART): ")
        currency = input("Enter the currency (e.g., USD): ")
        bar_size = int(input("Enter the bar size in seconds (e.g., 5, 10, 15): "))

        # Create a contract object and define its parameters
        contract = Contract()
        contract.symbol = symbol
        contract.secType = secType
        contract.exchange = exchange
        contract.currency = currency

        # Request real-time volume bar data
        self.reqRealTimeBars(1, contract, bar_size, "VOLUME", False, [])

    # ... [other methods] ...

    def realTimeBar(self, reqId, time, open, high, low, close, volume, wap, count):
        # Overridden method to receive real-time bar data
        print(f"Real-Time Bar. Time: {time}, Volume: {volume}")

    def request_bid_ask_data(self):
        # Prompt for user input
        symbol = input("Enter the symbol (e.g., AAPL): ")
        secType = input("Enter the security type (e.g., STK for stock): ")
        exchange = input("Enter the exchange (e.g., SMART): ")
        currency = input("Enter the currency (e.g., USD): ")

        # Create a contract object and define its parameters
        contract = Contract()
        contract.symbol = symbol
        contract.secType = secType
        contract.exchange = exchange
        contract.currency = currency

        # Request market data with bid-ask information
        self.reqMktData(1, contract, "225", False, False, [])
        # The generic tick type "225" requests bid-ask data

    def tickPrice(self, reqId, tickType, price, attrib):
        # Overridden method to receive price updates
        if tickType in [1, 2]:  # 1 for Bid Price, 2 for Ask Price
            print(f"TickType: {tickType}, Price: {price}")

    def tickSize(self, reqId, tickType, size):
        # Overridden method to receive size updates
        if tickType in [0, 3]:  # 0 for Bid Size, 3 for Ask Size
            print(f"TickType: {tickType}, Size: {size}")

    def live_data_main(self):
        # List of available data types
        data_types = {
            "1": "Candle Stick",  
            "2": "Tick by tick",  
            "3": "Time and sales", 
            "4": "Market depth",
            "5": "Volume", 
            "6": "Bid-Ask", 
        }

        # Display data type options
        print("What type of data would you like to stream?")
        for key, value in data_types.items():
            print(f"{key}. {value}")

        # User selects a data type
        data_choice = input("Enter your choice: ")
        selected_data_type = data_types.get(data_choice)

        if selected_data_type is None:
            print("Invalid choice.")
            return

        # Call the appropriate method based on the selected data type
        if selected_data_type == "Candle Stick":
            self.request_candlestick_data()
        elif selected_data_type == "Tick by tick":
            self.request_tick_by_tick_data()
        elif selected_data_type == "Time and sales":
            self.request_time_and_sales_data()
        elif selected_data_type == "Market depth":
            self.request_market_depth_data()
        # ... and so on for other data types
