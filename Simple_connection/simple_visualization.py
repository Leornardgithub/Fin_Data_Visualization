import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from collections import deque
import numpy as np

class LiveGraph(QMainWindow):
    def __init__(self):
        super().__init__()
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # Data buffer
        self.data = deque(maxlen=100)  # Adjust maxlen as needed

        # Set up the graph
        self.graphWidget.setBackground('white')
        self.graphWidget.setTitle("Real-Time Data Stream", color="black", size="30pt")
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot([], [], pen=self.pen)

        # Update the plot periodically
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(50)  # Time in ms

    def update_plot(self):
        # This method will receive and update the plot with new data
        if self.data:
            self.data_line.setData(range(len(self.data)), list(self.data))

    def add_data(self, value):
        # This method adds data to the buffer
        self.data.append(value)

