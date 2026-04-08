import system
import sys
import os

from system import process

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class Main:
        def __init__(self, input_str):
                print("Hello World")
                self.process = process.Process()
                

        def run(self):
                pass

if __name__ == "__main__":
    Main("Hello World")
