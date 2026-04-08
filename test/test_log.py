import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log.log import Log, Log_Level  # 注意导入方式

class TestLog(unittest.TestCase):
    def test_run(self):
        log_api = Log(Log_Level.DEBUG)
        log_api.set_data_persistence(os.path.join(os.path.dirname(__file__), "test.log"))
        log_api.log_debug("test debug")
        log_api.log_info("test info")
        log_api.log_warn("test warning")
        log_api.log_error("test error")
        
if __name__ == '__main__':
    unittest.main()