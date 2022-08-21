from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class RedditObject:
    score: int
    id: int
    authorName: str
    subreddit: str
    body: str
    isSubmission: bool = False
