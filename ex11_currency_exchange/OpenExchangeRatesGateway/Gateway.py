import os
import json

class Gateway():
    def __init__(self):
        pass

    def get_rates(self, static=True):
        if static:
            with open(os.path.join(os.path.dirname(__file__), 'static_exchange_rates.json'), 'r') as static_file:
                static_data = json.load(static_file)['rates']
            return static_data
        else:
            raise NotImplementedError("only static rates supported so far")
