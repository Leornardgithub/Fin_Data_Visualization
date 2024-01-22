from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from datetime import datetime, timezone
from threading import Thread

class HistoricalDataApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print(f"Error: {reqId} {errorCode} {errorString}")

    def historicalData(self, reqId, bar):
        print(f"Time: {bar.date}, Open: {bar.open}, High: {bar.high}, Low: {bar.low}, Close: {bar.close}, Volume: {bar.volume}")

    def run_loop(self):
        self.run()

def main():
    app = HistoricalDataApp()
    app.connect("127.0.0.1", 7497, clientId=1)

    thread = Thread(target=app.run_loop)
    thread.start()

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"

    # Convert local time to UTC and format the request date
    local_date = datetime(2024, 1, 19, 0, 0)
    utc_date = local_date.astimezone(timezone.utc).strftime("%Y%m%d %H:%M:%S")

    app.reqHistoricalData(
        reqId=1,
        contract=contract,
        endDateTime=utc_date,
        durationStr="1 D",
        barSizeSetting="1 hour",
        whatToShow="MIDPOINT",
        useRTH=1,
        formatDate=1,
        keepUpToDate=False,
        chartOptions=[]
    )

    input("Press Enter to exit\n")
    app.disconnect()
    thread.join()

if __name__ == "__main__":
    main()

