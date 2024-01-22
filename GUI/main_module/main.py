"""
This is the main file for running my program.
"""
from ibapi import client
from ibapi import wrapper

def main():
#create an instance of the IB_Connection class
    connection = client.Connection(host = "127.0.0.1", port = 7497)
    connection.connect()
    connection.disconnect()
    print("Connection to TWS closed.")
    return

if __name__ == "__main__":
    main()

