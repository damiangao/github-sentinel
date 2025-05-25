import asyncio
import logging
from datetime import datetime, timedelta
from pathlib import Path

import click
from rich.logging import RichHandler

from .core.config import Config, load_config, save_config
from .core.github_client import GitHubClient
from .notifiers.base import EmailNotifier, SlackNotifier, WebhookNotifier

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger("github_sentinel")


@click.group()
def cli():
    """GitHub Sentinel - GitHub 仓库监控工具"""
    pass


@cli.command()
@click.option("--config", type=click.Path(), default="~/.github_sentinel/config.yaml")
def init(config):
    """初始化配置文件"""
    config_path = Path(config).expanduser()
    if config_path.exists():
        click.echo(f"配置文件已存在: {config_path}")
        return

    config_path.parent.mkdir(parents=True, exist_ok=True)
    default_config = Config(github_token="")
    save_config(default_config, config_path)
    click.echo(f"配置文件已创建: {config_path}")


@cli.command()
@click.argument("repo")
@click.option("--config", type=click.Path(), default="~/.github_sentinel/config.yaml")
def subscribe(repo, config):
    """订阅仓库"""
    config_path = Path(config).expanduser()
    if not config_path.exists():
        click.echo("请先运行 init 命令创建配置文件")
        return

    config_data = load_config(config_path)
    owner, repo_name = repo.split("/")
    config_data.repositories.append(
        RepositoryConfig(owner=owner, repo=repo_name)
    )
    save_config(config_data, config_path)
    click.echo(f"已订阅仓库: {repo}")


@cli.command()
@click.option("--config", type=click.Path(), default="~/.github_sentinel/config.yaml")
def start(config):
    """启动监控"""
    config_path = Path(config).expanduser()
    if not config_path.exists():
        click.echo("请先运行 init 命令创建配置文件")
        return

    config_data = load_config(config_path)
    if not config_data.github_token:
        click.echo("请在配置文件中设置 GitHub Token")
        return

    asyncio.run(run_monitor(config_data))


async def run_monitor(config: Config):
    """运行监控"""
    client = GitHubClient(config.github_token)
    notifiers = []

    if config.notification.email:
        notifiers.append(
            EmailNotifier(
                smtp_server="smtp.gmail.com",
                smtp_port=587,
                username=config.notification.email,
                password="",  # TODO: 从环境变量或安全存储获取
            )
        )

    if config.notification.slack_webhook:
        notifiers.append(SlackNotifier(config.notification.slack_webhook))

    if config.notification.webhook_url:
        notifiers.append(WebhookNotifier(config.notification.webhook_url))

    while True:
        try:
            activities = []
            since = datetime.now() - timedelta(days=1)

            for repo_config in config.repositories:
                activity = client.get_repository_activity(
                    repo_config.owner,
                    repo_config.repo,
                    since,
                )
                activities.append(activity)

            for notifier in notifiers:
                await notifier.send(activities)

            await asyncio.sleep(3600)  # 每小时检查一次

        except Exception as e:
            logger.exception("监控过程中发生错误")
            await asyncio.sleep(300)  # 发生错误时等待5分钟后重试


if __name__ == "__main__":
    cli() 