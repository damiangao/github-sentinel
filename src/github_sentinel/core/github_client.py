from datetime import datetime, timezone
from typing import Dict, List, Optional

from github import Github
from github.Repository import Repository

from ..models.repository import (
    Commit,
    Issue,
    PullRequest,
    Release,
    RepositoryActivity,
)


class GitHubClient:
    """GitHub API 客户端"""

    def __init__(self, token: str):
        self.client = Github(token, per_page=30)  # 设置每页数量

    def get_repository(self, owner: str, repo: str) -> Repository:
        """获取仓库信息"""
        return self.client.get_repo(f"{owner}/{repo}")

    def get_recent_commits(
        self, repo: Repository, since: datetime, max_count: int = 20
    ) -> List[Commit]:
        """获取最近的提交"""
        print("正在获取提交信息...")
        commits = []
        for commit in repo.get_commits(since=since):
            commits.append(
                Commit(
                    sha=commit.sha,
                    message=commit.commit.message,
                    author=commit.commit.author.name,
                    date=commit.commit.author.date,
                )
            )
            if len(commits) % 10 == 0:
                print(f"已获取 {len(commits)} 条提交")
            if len(commits) >= max_count:
                break
        return commits

    def get_recent_issues(
        self, repo: Repository, since: datetime, max_count: int = 20
    ) -> List[Issue]:
        """获取最近的问题"""
        print("正在获取问题信息...")
        issues = []
        for issue in repo.get_issues(state="all", since=since):
            issues.append(
                Issue(
                    number=issue.number,
                    title=issue.title,
                    state=issue.state,
                    author=issue.user.login,
                    created_at=issue.created_at,
                    updated_at=issue.updated_at,
                )
            )
            if len(issues) % 10 == 0:
                print(f"已获取 {len(issues)} 个问题")
            if len(issues) >= max_count:
                break
        return issues

    def get_recent_pull_requests(
        self, repo: Repository, since: datetime, max_count: int = 20
    ) -> List[PullRequest]:
        """获取最近的拉取请求"""
        print("正在获取拉取请求信息...")
        # 确保 since 为带时区的 UTC 时间
        if since.tzinfo is None:
            since = since.replace(tzinfo=timezone.utc)
        prs = []
        for pr in repo.get_pulls(state="all"):
            if pr.created_at > since:
                prs.append(
                    PullRequest(
                        number=pr.number,
                        title=pr.title,
                        state=pr.state,
                        author=pr.user.login,
                        created_at=pr.created_at,
                        updated_at=pr.updated_at,
                    )
                )
                if len(prs) % 5 == 0:
                    print(f"已获取 {len(prs)} 个拉取请求")
                if len(prs) >= max_count:
                    break
        return prs

    def get_recent_releases(
        self, repo: Repository, since: datetime, max_count: int = 10
    ) -> List[Release]:
        """获取最近的发布"""
        print("正在获取发布信息...")
        # 确保 since 为带时区的 UTC 时间
        if since.tzinfo is None:
            since = since.replace(tzinfo=timezone.utc)
        releases = []
        for release in repo.get_releases():
            created_at = release.created_at
            if created_at.tzinfo is None:
                created_at = created_at.replace(tzinfo=timezone.utc)
            if created_at > since:
                releases.append(
                    Release(
                        tag_name=release.tag_name,
                        name=release.title,
                        body=release.body,
                        author=release.author.login,
                        created_at=release.created_at,
                    )
                )
                if len(releases) % 2 == 0:
                    print(f"已获取 {len(releases)} 个发布")
                if len(releases) >= max_count:
                    break
        return releases

    def get_repository_activity(
        self, owner: str, repo: str, since: datetime,
        max_count: int = 20
    ) -> RepositoryActivity:
        """获取仓库活动"""
        print(f"开始获取 {owner}/{repo} 的仓库活动...")
        repository = self.get_repository(owner, repo)
        return RepositoryActivity(
            owner=owner,
            repo=repo,
            commits=self.get_recent_commits(repository, since, max_count),
            issues=self.get_recent_issues(repository, since, max_count),
            pull_requests=self.get_recent_pull_requests(repository, since, max_count),
            releases=self.get_recent_releases(repository, since, max_count // 10),
        ) 