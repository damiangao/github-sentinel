# GitHub Sentinel v0.0.1

这是 GitHub Sentinel 的第一个 alpha 版本，提供了基本的项目框架和核心功能实现。

## 🚀 新特性

### 核心功能
- 基础项目结构搭建
- 配置管理系统
- GitHub API 客户端封装
- 数据模型定义
- 通知系统框架

### 命令行工具
- 初始化配置 (`init`)
- 仓库订阅管理 (`subscribe`)
- 监控启动 (`start`)

## 📦 技术栈
- Python 3.8+
- PyGithub
- Pydantic
- Click
- Rich
- aiohttp

## 🔧 配置选项
- GitHub Token 配置
- 仓库订阅管理
- 通知方式设置（邮件/Slack/Webhook）
- 监控频率设置

## ⚠️ 已知问题
- 配置文件加载/保存逻辑待实现
- 通知器具体实现待完成
- 数据持久化功能待添加
- 错误处理机制待完善

## 📝 待办事项
- [ ] 实现配置文件的具体加载和保存逻辑
- [ ] 完善通知器的具体实现
- [ ] 添加更多的通知模板
- [ ] 实现数据持久化
- [ ] 添加更多的监控选项
- [ ] 添加测试用例
- [ ] 完善错误处理
- [ ] 添加日志记录
- [ ] 实现更多的通知方式

## 🔍 使用说明

1. 安装：
```bash
pip install github-sentinel
```

2. 初始化配置：
```bash
github-sentinel init
```

3. 订阅仓库：
```bash
github-sentinel subscribe owner/repo
```

4. 启动监控：
```bash
github-sentinel start
```

## 🤝 贡献指南

欢迎提交 Pull Requests 和 Issues！请确保：
1. 遵循项目的代码风格
2. 添加适当的测试
3. 更新相关文档

## ⚖️ 许可证

MIT License 