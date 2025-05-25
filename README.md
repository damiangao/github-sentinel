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

### 进阶特性
- 支持对 GitHub 仓库数据抓取数量进行限制，提升大仓库兼容性和执行效率
- 自动处理时区差异，兼容不同时间格式

## 📦 技术栈
- Python 3.8+
- PyGithub
- Pydantic
- Click
- Rich
- aiohttp

## 🔧 配置选项
- GitHub Token 配置
  - 在 GitHub 个人设置中生成 Personal Access Token (Settings -> Developer settings -> Personal access tokens)
  - 运行 `github-sentinel init` 时输入 token，或手动编辑配置文件
  - Token 需要以下权限：
    - `repo` (完整仓库访问权限)
    - `notifications` (通知访问权限)
    - `read:org` (组织访问权限，如果需要监控组织仓库)
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

5. （可选）自定义数据抓取数量
如需在脚本或集成中限制抓取的提交、Issue、PR、Release数量，可通过 `max_count` 参数设置，避免大仓库超时。

## 🤝 贡献指南

欢迎提交 Pull Requests 和 Issues！请确保：
1. 遵循项目的代码风格
2. 添加适当的测试
3. 更新相关文档

## ⚖️ 许可证

MIT License
