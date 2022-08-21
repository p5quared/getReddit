import os

import praw
from dotenv import load_dotenv
from pprint import pprint

from classes import RedditObject

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
print(f'Reddit instance established?\n{reddit.read_only}\n')

saved_comments = list()
submissions = reddit.subreddit('askreddit').hot(limit=3)
gathered_content = list()

# Works for text based Q/A subs i.e. r/askreddit, r/askmen...
for n, submission in enumerate(submissions):
    post = {"submission": None, "comments": list()}  # container for submission & comments
    submission.comments.replace_more(limit=0)
    post["submission"] = RedditObject(submission.score,
                                      submission.id,
                                      submission.author.name,
                                      submission.subreddit.name,
                                      body=submission.title,
                                      isSubmission=True)

    print("Getting comments...")
    comment_forest = submission.comments
    gathered_text = str()
    for surface_comment in comment_forest[:10]:  # get top x comments
        if surface_comment.author is None:
            safe_author_name = "deleted"
        else:
            safe_author_name = surface_comment.author.name

        post["comments"].append(RedditObject(
            surface_comment.score,
            surface_comment.id,
            authorName=safe_author_name,
            subreddit=surface_comment.subreddit.name,
            body=surface_comment.body,
            isSubmission=False,
        ))
        gathered_text += surface_comment.body
        # for .replies to get replies to comments
    gathered_content.append(post)
    print(len(post["comments"]), "gathered from current post...")

pprint(gathered_content)
