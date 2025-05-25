# GitHub Sentinel

GitHub Sentinel 是一款开源工具类 AI Agent，专为开发者和项目管理人员设计，能够定期（每日/每周）自动获取并汇总订阅的 GitHub 仓库最新动态。

## 主要功能

- 订阅管理：轻松添加、删除和管理 GitHub 仓库订阅
- 更新获取：自动获取订阅仓库的最新动态
- 通知系统：支持多种通知方式（邮件、Slack、Webhook等）
- 报告生成：生成定期更新报告，包含重要变更和统计信息

## 安装

```bash
pip install github-sentinel
```

## 快速开始

1. 配置 GitHub Token：
```bash
export GITHUB_TOKEN=your_github_token
```

2. 创建配置文件：
```bash
github-sentinel init
```

3. 添加仓库订阅：
```bash
github-sentinel subscribe owner/repo
```

4. 启动监控：
```bash
github-sentinel start
```

## 配置选项

- 通知频率：每日/每周
- 通知方式：邮件/Slack/Webhook
- 监控内容：Issues/PRs/Commits/Releases

## 贡献

欢迎提交 Pull Requests 和 Issues！

## 许可证

MIT License
