import akshare as ak
import pandas as pd
import time
import os

class Input:
        def __init__(self):
                print("Input Class")
                
        def get_all_A_stocks_info(self):
                
                self.all_Astocks_df = ak.stock_zh_a_spot()
                