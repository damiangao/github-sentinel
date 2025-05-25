from pathlib import Path
from typing import Dict, List, Optional

import yaml
from pydantic import BaseModel, Field


class NotificationConfig(BaseModel):
    """通知配置模型"""
    email: Optional[str] = None
    slack_webhook: Optional[str] = None
    webhook_url: Optional[str] = None
    frequency: str = "daily"  # daily or weekly


class RepositoryConfig(BaseModel):
    """仓库配置模型"""
    owner: str
    repo: str
    watch_issues: bool = True
    watch_prs: bool = True
    watch_commits: bool = True
    watch_releases: bool = True


class Config(BaseModel):
    """主配置模型"""
    github_token: str
    repositories: List[RepositoryConfig] = Field(default_factory=list)
    notification: NotificationConfig = Field(default_factory=NotificationConfig)
    data_dir: Path = Field(default=Path.home() / ".github_sentinel")

    class Config:
        arbitrary_types_allowed = True


def load_config(config_path: Path) -> Config:
    """加载配置文件"""
    if not config_path.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        config_data = yaml.safe_load(f)

    return Config(**config_data)


def save_config(config: Config, config_path: Path) -> None:
    """保存配置文件"""
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    config_data = config.dict()
    # 将 Path 对象转换为字符串
    config_data["data_dir"] = str(config_data["data_dir"])
    
    with open(config_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(config_data, f, allow_unicode=True, sort_keys=False) 