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

# 清除代理环境变量（防止代理冲突）
for key in [
    "http_proxy",
    "https_proxy",
    "all_proxy",
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
]:
    os.environ.pop(key, None)
os.environ["NO_PROXY"] = "*"


class Launch:
        def __init__(self, log_handle: Log):
                self.log_handle = log_handle
                self.log_handle.log_info("Launch initialized")
                
        def get_all_Ashare_realtime_stocks_info(self):
                self.log_handle.log_info("获取当前沪深京A股所有上市公司的实时行情数据")
                self.all_stocks_df = ak.stock_zh_a_spot()
       
        def get_target_stock_info(self, stock_code: str):
                self.log_handle.log_info(f"获取目标股票 {stock_code} 的实时行情数据")
                target_stock_info_df = ak.stock_individual_info_em(stock_code)
                return target_stock_info_df
        
        def get_target_stock_market_quotation(self, stock_code: str):
                self.log_handle.log_info(f"获取目标股票 {stock_code} 的市场价格数据")
                target_stock_market_q = ak.stock_bid_ask_em(stock_code)
                return target_stock_market_q
                