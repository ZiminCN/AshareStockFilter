import time
import os
from enum import Enum

class Log_Level(Enum):
        DEBUG = 0
        INFO = 1
        WARN = 2
        ERROR = 3

class Log:
        def __init__(self, Log_Level):
                self.log_level = Log_Level
                self.log_file = None
    
        def set_data_persistence(self, file):
                file_dir = os.path.dirname(file)
                if file_dir and not os.path.exists(file_dir):
                        os.makedirs(file_dir, exist_ok=True)
                        print(f"创建日志目录: [{file_dir}]")
                
                # 如果文件不存在，创建它
                if not os.path.exists(file):
                        try:
                                with open(file, 'w', encoding='utf-8') as f:
                                        pass  # 创建空文件
                                print(f"创建日志文件: [{file}]")
                        except Exception as e:
                                print(f"创建日志文件失败: [{file}], 错误: {e}")
                                return False
                self.log_file = file
        
        def file_write(self, Log_Level, message):
                if not os.path.exists(self.log_file):
                        pass
                with open(self.log_file, 'a') as f:
                        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}][{Log_Level}]: {message}\n")
        
        def log_debug(self, message):
                if self.log_level.value >= Log_Level.DEBUG.value:
                        pass
                self.file_write("Debug", message)
        
        def log_info(self, message):
                if self.log_level.value >= Log_Level.INFO.value:
                        pass
                self.file_write("Info", message)
        
        def log_warn(self, message):
                if self.log_level.value >= Log_Level.WARN.value:
                        pass
                self.file_write("Warn", message)
        
        def log_error(self, message):
                if self.log_level.value >= Log_Level.ERROR.value:
                        pass
                self.file_write("Error", message)
