"""module for managing the connection to TWS/IB Gateway"""
"""
The Class that manages the connections to tws/ ib gateway,
opening the connection, manageging communication and closing the connection.
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from threading import Thread

import time
import keyboard

class IBConnectionManager(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.server_version = None
        self.connection_time = None
        self.connection_check_interval = 30 #seconds
 
    def error(self, reqId, errorCode, errorString):
        print(f"connection: {reqId} {errorCode} {errorString}")
    
    def connect_to_tws(self, host="127.0.0.1", port=7497, clientId=1):
        """
        Connects to TWS or IB Gateway.
        :param host: Hostname or IP.
        :param port: Port number.
        :param clientId: Client ID.
        """
        super().connect(host, port, clientId)

        # Start the run loop in a separate thread
        Thread(target=self.run, daemon=True).start()

        # Give time for the connection to be established
        time.sleep(0.5)

        if not super().isConnected():
            print("Failed to connect to TWS/IB Gateway")
            return False
        
        #Start a daemon thread to monitor the connection
        Thread(target=self.monitor_connection, daemon=True).start()

        self.reqCurrentTime()
        self.server_version = super().serverVersion()
        self.connection_time = super().twsConnectionTime()
        
        print("Successfully connected to TWS/IB Gateway")
        print(f"Server version:{self.server_version}")
        print(f"Connection TIme:{self.connection_time}")
        
        return True
    
    def monitor_connection(self):
        """
        Monitors the connection to TWS/IB Gateway.If the connection is lost, it will try to reconnect.
        """
        while True:
            time.sleep(self.connection_check_interval)
            if not super().isConnected():
                print("Connection lost, reconnecting...")
                self.connect_to_tws()
                if super().isConnected():
                    print("Successfully reconnected")
                else:
                    print("Failed to reconnect")
    
    def currentTime(self, time: int):
        print(f"Current time: {time}")
        return super().currentTime(time)
    
    def start_keyboard_listener(self, disconnect_key='q'):
        """
        Starts a thread that listens for a specific keyboard character to disconnect.
        :param disconnect_key: The keyboard character that triggers the disconnection.
        """
        Thread(target=self.keyboard_listener, args=(disconnect_key,), daemon=True).start()

    def keyboard_listener(self, disconnect_key):
        """
        Listens for the disconnect key and triggers a disconnection from TWS.
        :param disconnect_key: The keyboard character that triggers the disconnection.
        """
        print(f"Press '{disconnect_key}' to disconnect from TWS.")
        keyboard.wait(disconnect_key)  # Wait until the disconnect key is pressed
        print("Disconnect key pressed. Disconnecting from TWS...")
        self.disconnect_from_tws()
        
    def disconnect_from_tws(self):
        """ Disconnects from TWS/IB Gateway """
        if self.isConnected():
            print("Disconnecting from TWS/IB Gateway...")
            self.disconnect()
            print("Disconnected from TWS/IB Gateway.")
        else:
            print("Already disconnected.")
     
    # You can add other methods here as needed

        