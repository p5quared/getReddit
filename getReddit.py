import os
import dotenv

import praw

from classes import RedditObject, Post

reddit = praw.Reddit(
    client_id=os.environ['CLIENT_ID'],
    client_secret=os.environ['CLIENT_SECRET'],
    user_agent=f'requests for my Youtube maker script (u/pto2)'
)


def getReddit(sub, num_posts, comments_per_post)->list:
    gathered_posts = list()
    reddit_submissions = reddit.subreddit(sub).top(limit=num_posts, time_filter="day")
    for n, submission in enumerate(reddit_submissions):
        submission.comments.replace_more(limit=0)
        new_post = Post(RedditObject(
            submission.score,
            submission.id,
            submission.author.name,
            submission.subreddit.name,
            body=submission.title,
            isSubmission=True
        ))
        for surface_comment in submission.comments[:comments_per_post]:  # number of comments to retrieve
            if surface_comment.author is None:
                safe_author_name = "deleted"
            else:
                safe_author_name = surface_comment.author.name
            new_post.comments.append(RedditObject(
                surface_comment.score,
                surface_comment.id,
                safe_author_name,
                surface_comment.subreddit.name,
                body=surface_comment.body
            ))
        print(f"{n + 1} POST(s) GATHERED")
        gathered_posts.append(new_post)
    return gathered_posts




if __name__ == '__main__':
    print(f'Reddit instance established?.....\n{reddit.read_only}\n')
