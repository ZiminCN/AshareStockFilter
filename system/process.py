# Copyright (c) Direct Drive Technology Co., Ltd. All rights reserved.
# Author: Zi Min <jianming.zeng@directdrivetech.com>
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

import sys
import os

from . import input

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.log import Log


class Process:
        def __init__(self, log_handle: Log):
                self.input = input.Input()
                self.log_handle = log_handle
                self.log_handle.log_info("Process init")
