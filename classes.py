from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class RedditObject:
    score: int
    id: int
    authorName: str
    subreddit: str
    body: str
    isSubmission: bool = False
    isReply: bool = False


class Post:
    head: RedditObject
    comments: [RedditObject]
    isMovie: bool = False

    def __init__(self, head):
        self.head = head
        self.id = head.id
        self.comments = list()
