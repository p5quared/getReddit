from getReddit import getReddit

if __name__ == '__main__':
    print("GETTING TEST POSTS:")
    testPosts = getReddit('askmen', num_posts=1, comments_per_post=10)
    for post in testPosts:
        post.write_movie()
