from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time
import random

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.done = False

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def tickPrice(self, reqId, tickType, price, attrib):
        print("Tick Price. Ticker Id:", reqId, "tickType:", tickType, "Price:", price)
        
    def disconnect_from_tws(self):
        self.cancelMktData(1)  # Cancel the market data subscription
        self.done = True
        self.disconnect()
        print("Disconnected from TWS")

    def force_disconnect(self):
        self.done = True
        self.disconnect()
        print("Forcefully disconnected from TWS")

def main():
    time.sleep(5) # Give enough time for the IB Gateway to load
    print("Starting the main function")
    clientId = random.randint(0, 10000)  # Generate a random client ID
    
    def run_loop():
        while not app.done:
            app.run() 
        print("Exiting the IB API loop")
    print("BOOB")
    # Initialize and connect
    app = TestApp()
    app.connect("127.0.0.1", 7497, clientId=0)
    print("Connected to TWS")
    # Start the API in a separate thread
    api_thread = threading.Thread(target=run_loop)
    api_thread.start()

    # Define a Contract for NQ Futures March 2024
    contract = Contract()
    contract.symbol = "NQ"
    contract.secType = "FUT"
    contract.exchange = "CME"
    contract.currency = "USD"
    contract.lastTradeDateOrContractMonth = "202403"

    # Request Market Data
    app.reqMktData(1, contract, "", False, False, [])

    # Run for a short period
    time.sleep(10)

    # Forcefully disconnect and terminate threads
    app.disconnect_from_tws()
    api_thread.join(timeout=5)  # Timeout for joining the thread

    # Attempt to forcefully terminate the thread if it's still alive
    if api_thread.is_alive():
        print("Thread is still alive, attempting to forcefully terminate it.")
        # You can use more aggressive methods here if necessary, such as os._exit(0), but be cautious.
    else:
        print("Thread terminated successfully.")

    # No join is called on the thread in this forceful approach

if __name__ == "__main__":
    main()
