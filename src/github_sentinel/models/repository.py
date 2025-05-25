from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Commit(BaseModel):
    """提交模型"""
    sha: str
    message: str
    author: str
    date: datetime


class Issue(BaseModel):
    """问题模型"""
    number: int
    title: str
    state: str
    author: str
    created_at: datetime
    updated_at: datetime


class PullRequest(BaseModel):
    """拉取请求模型"""
    number: int
    title: str
    state: str
    author: str
    created_at: datetime
    updated_at: datetime


class Release(BaseModel):
    """发布模型"""
    tag_name: str
    name: str
    body: Optional[str]
    author: str
    created_at: datetime


class RepositoryActivity(BaseModel):
    """仓库活动模型"""
    owner: str
    repo: str
    commits: List[Commit] = []
    issues: List[Issue] = []
    pull_requests: List[PullRequest] = []
    releases: List[Release] = [] 