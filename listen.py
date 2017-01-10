#!/usr/bin/env python
# sudo python listen.py
import json
import time
import math
import thread
import sys
sys.path.insert(0, '../noob')
from noob import *

class ButtonListener:

    def initialize(self):

        # D8 on the GrovePI shield
        self.button = Button().initialize({
          'name': "Button",
          'digitalPort': 8,
          'pinMode': "INPUT"
        })
        return self

    def listening(self):
        while True:
            try:
                button_value = self.button.digitalRead()

                print("button:" + str(button_value))

                time.sleep(1)

            except (IOError,TypeError) as e:
                print e

# main

buttonListener = ButtonListener().initialize()

try:
  thread.start_new_thread( buttonListener.listening, () )

except Exception as e:
   print e

while 1:
  pass
