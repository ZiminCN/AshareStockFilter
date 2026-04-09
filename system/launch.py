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
                
        def get_all_A_stocks_info(self):
                self.log_handle.log_info("获取所有沪深京A股上市公司的实时行情数据")
                self.all_Astocks_df = ak.stock_zh_a_spot()