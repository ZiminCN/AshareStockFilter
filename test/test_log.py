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

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.log import Log, Log_Level


class TestLog(unittest.TestCase):
    def test_run(self):
        log_api = Log(Log_Level.DEBUG)
        log_api.set_data_persistence(
            os.path.join(os.path.dirname(__file__), "test_log/test.log")
        )
        log_api.log_debug("test debug")
        log_api.log_info("test info")
        log_api.log_warn("test warning")
        log_api.log_error("test error")


if __name__ == "__main__":
    unittest.main()
