from abc import ABC, abstractmethod
from typing import List

from ..models.repository import RepositoryActivity


class Notifier(ABC):
    """通知器基类"""

    @abstractmethod
    async def send(self, activities: List[RepositoryActivity]) -> None:
        """发送通知"""
        pass


class EmailNotifier(Notifier):
    """邮件通知器"""

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    async def send(self, activities: List[RepositoryActivity]) -> None:
        # TODO: 实现邮件发送逻辑
        pass


class SlackNotifier(Notifier):
    """Slack 通知器"""

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    async def send(self, activities: List[RepositoryActivity]) -> None:
        # TODO: 实现 Slack 消息发送逻辑
        pass


class WebhookNotifier(Notifier):
    """Webhook 通知器"""

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    async def send(self, activities: List[RepositoryActivity]) -> None:
        # TODO: 实现 Webhook 调用逻辑
        pass 