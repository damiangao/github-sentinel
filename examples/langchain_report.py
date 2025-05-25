import asyncio
import os
import signal
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from github_sentinel.core.github_client import GitHubClient
from github_sentinel.utils.report import ReportGenerator

# 加载环境变量
load_dotenv(Path(__file__).parent.parent / "config" / ".env")

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("操作超时")

async def main():
    print("开始执行...")
    
    # 设置超时处理
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(120)  # 120秒超时
    
    try:
        # 获取 GitHub Token
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise ValueError("请设置 GITHUB_TOKEN 环境变量")
        print("已获取 GitHub Token")

        # 创建 GitHub 客户端
        client = GitHubClient(token)
        print("已创建 GitHub 客户端")

        # 获取 langchain 仓库的活动
        since = datetime.now() - timedelta(days=7)  # 获取最近7天的活动
        print(f"开始获取仓库活动，时间范围：{since} 至今")
        
        try:
            print("正在获取提交信息...")
            activity = client.get_repository_activity("langchain-ai", "langchain", since, max_count=20)
            print("成功获取仓库活动")
        except Exception as e:
            print(f"获取仓库活动时出错：{str(e)}")
            raise

        # 生成报告
        report_generator = ReportGenerator()
        print("开始生成报告...")
        
        # 生成控制台报告
        print("\n=== 控制台报告 ===\n")
        report_generator.generate_console_report([activity])
        
        # 生成 HTML 报告
        html_report = report_generator.generate_html_report([activity])
        print("HTML 报告生成完成")
        
        # 保存 HTML 报告
        output_dir = Path("reports")
        output_dir.mkdir(exist_ok=True)
        
        report_path = output_dir / f"langchain_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(html_report)
        
        print(f"\nHTML 报告已保存到: {report_path}")
        
    except TimeoutError:
        print("操作超时，请检查网络连接或 GitHub API 状态")
    except Exception as e:
        print(f"发生错误：{str(e)}")
    finally:
        # 取消超时
        signal.alarm(0)

if __name__ == "__main__":
    asyncio.run(main()) 