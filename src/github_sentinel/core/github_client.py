from datetime import datetime
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
        self.client = Github(token)

    def get_repository(self, owner: str, repo: str) -> Repository:
        """获取仓库信息"""
        return self.client.get_repo(f"{owner}/{repo}")

    def get_recent_commits(
        self, repo: Repository, since: datetime
    ) -> List[Commit]:
        """获取最近的提交"""
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
        return commits

    def get_recent_issues(
        self, repo: Repository, since: datetime
    ) -> List[Issue]:
        """获取最近的问题"""
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
        return issues

    def get_recent_pull_requests(
        self, repo: Repository, since: datetime
    ) -> List[PullRequest]:
        """获取最近的拉取请求"""
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
        return prs

    def get_recent_releases(
        self, repo: Repository, since: datetime
    ) -> List[Release]:
        """获取最近的发布"""
        releases = []
        for release in repo.get_releases():
            if release.created_at > since:
                releases.append(
                    Release(
                        tag_name=release.tag_name,
                        name=release.title,
                        body=release.body,
                        author=release.author.login,
                        created_at=release.created_at,
                    )
                )
        return releases

    def get_repository_activity(
        self, owner: str, repo: str, since: datetime
    ) -> RepositoryActivity:
        """获取仓库活动"""
        repository = self.get_repository(owner, repo)
        return RepositoryActivity(
            owner=owner,
            repo=repo,
            commits=self.get_recent_commits(repository, since),
            issues=self.get_recent_issues(repository, since),
            pull_requests=self.get_recent_pull_requests(repository, since),
            releases=self.get_recent_releases(repository, since),
        ) 