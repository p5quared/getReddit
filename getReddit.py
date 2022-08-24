import praw
import os
from dotenv import load_dotenv

from classes import RedditObject, Post

load_dotenv()
USER_ID = os.getenv('USER_ID')
USER_PASSWORD = os.getenv('USER_PASSWORD')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=f'python: PMAW request enrichment (by u/pto2)'
)
print(f'Reddit instance established?.....\n{reddit.read_only}\n')


def getReddit(sub, num_posts):
    gathered_posts = list()
    reddit_submissions = reddit.subreddit(sub).hot(limit=num_posts)
    for n, submission in enumerate(reddit_submissions):
        submission.comments.replace_more(limit=0)
        nPost = Post(RedditObject(
            submission.score,
            submission.id,
            submission.author.name,
            submission.subreddit.name,
            body=submission.title,
            isSubmission=True
        ))
        for surface_comment in submission.comments[:10]:
            if surface_comment.author is None:
                safe_author_name = "deleted"
            else:
                safe_author_name = surface_comment.author.name
            nPost.comments.append(RedditObject(
                surface_comment.score,
                surface_comment.id,
                surface_comment.author.name,
                surface_comment.subreddit.name,
                body=surface_comment.body
            ))
        print(f"{n + 1} POST(s) GATHERED")
        gathered_posts.append(nPost)
    return gathered_posts
