# ibapi_historical_data.py

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Thread

class HistoricalDataManager(EWrapper, EClient):
    """Serves as the client and the wrapper"""
    """
    Ib historical data methods:
        -reqHistoricalData: Request historical data
            -cancelHistoricalData: Cancel historical data
            
        -reqHeadTimeStamp: Request historical data head time stamp
            -cancelHeadTimeStamp: Cancel historical data head time stamp
            
        -req/historicalTicks: Request historical ticks
            -cancelHistoricalTicks: Cancel historical ticks
            
        -reqContractDetails: Request contract details
            -cancelContractDetails: Cancel contract details
    """
    
    def __init__(self):
        EClient.__init__(self, self)

    def historical_data_main(self):
        # Prompt for user input
        asset_class = input("What asset class would you like? ")
        symbol = input("What Symbol? ")
        data_type = input("What Data Type? (e.g., Bar data, Volume, etc.): ")
        time_frame = input("What time frame? (e.g., 1 D, 1 W, 1 M): ")
        exchange = input("What exchange? ")
        duration = input("Enter the duration for historical data (e.g., 1 D, 1 W, 1 M): ")
        bar_size = input("Enter the bar size (e.g., 1 hour, 1 day): ")

        # Call method to request historical data
        self.request_historical_data(symbol, secType=asset_class, exchange=exchange, duration=duration, bar_size=bar_size, what_to_show=data_type)

    def request_historical_data(self, symbol, secType, exchange, duration, bar_size, what_to_show):
        # Logic to request historical data based on user input
        contract = self.create_contract(symbol, secType, exchange)
        self.reqHistoricalData(1, contract, "", duration, bar_size, what_to_show, 1, 1, False, [])
        # Add additional logic as needed

    def create_contract(self, symbol, secType, exchange):
        # Create and return a contract
        contract = Contract()
        contract.symbol = symbol
        contract.secType = secType
        contract.exchange = exchange
        return contract

    # Overridden methods from EWrapper for handling historical data callbacks
    # Other necessary methods...


