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

#!/bin/bash
current_dir=$(pwd)

if [ -d "$current_dir/output" ]; then
    rm -rf $current_dir/output
fi

if [ -d "$current_dir/test/test_log" ]; then
    rm -rf $current_dir/test/test_log
fi

if [ -d "$current_dir/system/__pycache__" ]; then
    rm -rf $current_dir/system/__pycache__
fi

if [ -d "$current_dir/log/__pycache__" ]; then
    rm -rf $current_dir/log/__pycache__
fi

if [ -d "$current_dir/strategy/__pycache__" ]; then
    rm -rf $current_dir/strategy/__pycache__
fi

if [ -d "$current_dir/filter/__pycache__" ]; then
    rm -rf $current_dir/filter/__pycache__
fi