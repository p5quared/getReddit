import os
import praw
from dotenv import load_dotenv
from pprint import pprint

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
'''
<< notes on PRAW >> 
reddit.subreddit("abc")
submissions
    .title
    .body
    .score
    .comments[n]
     [n].body
        .replies[n]
         [n].body
.replace_more(limit=0) >> eliminates "more comments"
'''
#  get title & top 3 comment chains (max 3 levels deep),
#  from top post on subreddit
saved_comments = list()
submissions = reddit.subreddit('askreddit').hot(limit=1)
with open("subtext.txt", "w") as f:
    # TODO: cleanup usage of f.write()... append all to [[],[]] and use .writelines()

    # TODO: remove print statements/differentiate whether to print output or write output
    #       (eventually prints will almost certainly be eliminated)

    # Works for text based reply subs (r/askreddit, r/askmen, etc...)
    for n, submission in enumerate(submissions):
        submission.comments.replace_more(limit=0)
        print(n+1, submission.title)
        f.write("TITLE\n")
        f.write(submission.title + "\n")
        f.write("COMMENTS\n")
        comment_forest = submission.comments
        for surface_comment in comment_forest[:5]:  # get top 5 comments
            print("*"*8)
            print(surface_comment.body)
            f.write(">" + surface_comment.body + "\n")
            for reply in surface_comment.replies:  # get 2 replies if their scores meet criteria
                if reply.score >= (surface_comment.score / 2):
                    print(reply.body)
                    f.write("\t>"+reply.body+"\n")
f.close()
