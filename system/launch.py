# Copyright (c) 2026 Ziminyo. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import akshare as ak
import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.log import Log

class Launch:
        def __init__(self, log_handle: Log):
                self.log_handle = log_handle
                self.log_handle.log_info("Launch initialized")
                
        def get_all_Ashare_stocks_info(self):
                self.log_handle.log_info("获取沪深京A股所有上市公司的实时行情数据")
                self.all_stocks_df = ak.stock_sh_a_spot_em()
                
        def get_all_Ashare_industry_sector_info(self):
                self.log_handle.log_info("获取沪深京A股所有板块的成交数据")
                self.all_sector_df = ak.stock_szse_sector_summary()
                
        def get_target_stock_info(self, stock_code: str):
                self.log_handle.log_info(f"获取目标股票 {stock_code} 的实时行情数据")
                target_stock_info_df = ak.stock_individual_info_em(stock_code)
                return target_stock_info_df
        
        def get_target_stock_market_quotation(self, stock_code: str):
                self.log_handle.log_info(f"获取目标股票 {stock_code} 的市场价格数据")
                target_stock_market_q = ak.stock_bid_ask_em(stock_code)
                return target_stock_market_q
        
        

                