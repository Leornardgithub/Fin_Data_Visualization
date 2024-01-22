# main.py

import simple_visualization
import time
import ibapi
import datetime
from ibapi.client import EClient
from ibapi.decoder import EWrapper
from ibapi.contract import Contract
from ibapi_connection import IBConnectionManager
from ibapi_live_data import LiveDataManager
from ibapi_historical_data import HistoricalDataManager
from threading import Thread

def main():
    
    #this starts and maintains the connection to TWS
    ib_manager = IBConnectionManager()
    if ib_manager.connect_to_tws(host="127.0.0.1", port=7497, clientId=1):
       Thread(target=ib_manager.monitor_connection, daemon=True).start()
    # Connected, you can now start using the API
    
    #Either stream live data or request historical data
    # User prompt
    print("Please, select what you would like to do:")
    print("1. Stream live data")
    print("2. Request historical data")
    # Additional options can be added here

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        # Create an instance of LiveDataManager and call its method
        live_data = LiveDataManager()
        live_data.live_data_main()
        # Add any additional logic for live data streaming

    elif choice == '2':
        # Create an instance of HistoricalDataManager and call its method
        historical_data = HistoricalDataManager()
        historical_data.historical_data_main()
        # Add any additional logic for historical data retrieval

    else:
        print("Invalid choice.")

        # Additional options can be handled here
    

if __name__ == "__main__":
    main()
 
