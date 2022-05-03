from multiprocessing import Process
import revpimodio2

from random import randint
from time import sleep

from flask_socketio import SocketIO

class DataStreamer:
    def __init__(self):
        self._producer_socketio = SocketIO(message_queue='redis://') # for broadcasting data to connected clients
        self._producer_process = Process(target=self._produce, name="producer_process") # process to get data
        self._producer_process.start()

    def _produce(self):
        class DAQ:
            def __init__(self, socketio):
                self._produce_stream = False
                self._socketio = socketio
                # self._revpi = revpimodio2.RevPiModIO(autorefresh=True, debug=True)

            def _cycle_program(self, ct):
                if self._produce_stream:
                    new_data = randint(-500, 500)/100
                    # new_data = self._revpi.io.InputValue_1.value/1000
                    self._socketio.emit("new_data", {"data" : new_data})

            def produce(self):
                # self._revpi.cycleloop(self._cycle_program, cycletime=25)
                while True:
                    self._cycle_handler(1)
                    sleep(0.025)

        daq = DAQ(self._producer_socketio)
        daq.produce()
