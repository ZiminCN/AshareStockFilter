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
import akshare as ak
import pandas as pd
import time
import os

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


def get_limit_up_stocks():
    """
    获取今日A股涨停股票列表
    """
    print("正在获取A股实时行情数据，请稍候...")

    # 添加延迟，避免请求过快
    time.sleep(1)

    try:
        # 正确的接口：stock_zh_a_spot() - 获取A股实时行情
        df = ak.stock_zh_a_spot()

        if df.empty:
            print("未获取到数据，请检查网络连接")
            return pd.DataFrame()

        # 数据清洗
        df = df[df["名称"].notna()]
        df = df[df["名称"] != ""]

        # 转换涨跌幅为数值类型（涨跌幅列可能是字符串，如"10.01%"）
        # 需要先去除百分号再转换
        if "涨跌幅" in df.columns:
            # 如果涨跌幅是字符串格式（带%号）
            if df["涨跌幅"].dtype == "object":
                df["涨跌幅"] = df["涨跌幅"].str.replace("%", "").astype(float)
            else:
                df["涨跌幅"] = pd.to_numeric(df["涨跌幅"], errors="coerce")

        # 筛选涨停股（涨幅 >= 9.9%）
        df_limit_up = df[df["涨跌幅"] >= 9.9]

        if df_limit_up.empty:
            print("今日暂无涨停股票或数据未刷新。")
            return pd.DataFrame()

        # 按涨幅降序排序
        df_limit_up = df_limit_up.sort_values(by="涨跌幅", ascending=False)

        # 选取关键列展示
        result_cols = ["代码", "名称", "最新价", "涨跌幅", "成交量", "成交额"]
        available_cols = [col for col in result_cols if col in df_limit_up.columns]
        result = df_limit_up[available_cols]

        # 重置索引
        result = result.reset_index(drop=True)

        return result

    except Exception as e:
        print(f"数据获取失败: {e}")
        print("提示：如果是网络问题，可以稍后再试")
        return pd.DataFrame()


def get_limit_up_stocks_with_retry(retry_times=3):
    """
    带重试机制的获取函数
    """
    for i in range(retry_times):
        if i > 0:
            print(f"\n第 {i + 1} 次尝试...")
        result = get_limit_up_stocks()

        if not result.empty:
            return result

        if i < retry_times - 1:
            print("等待 3 秒后重试...")
            time.sleep(3)

    return pd.DataFrame()


class TestAKLib(unittest.TestCase):
    def test_run(self):
        print("A股涨停股票筛选器")
        print("=" * 30)

        stocks = get_limit_up_stocks_with_retry()

        if not stocks.empty:
            print(f"\n✅ 今日涨停股票共 {len(stocks)} 只：")
            print("=" * 80)
            print(stocks.to_string(index=False))
            print("=" * 80)
        else:
            print("\n❌ 未能获取到涨停股票数据")
            print("可能原因：")
            print("1. 当前是非交易时间（数据不更新）")
            print("2. 网络连接问题")
            print("3. 今日确实没有涨停股票")


if __name__ == "__main__":
    unittest.main()
