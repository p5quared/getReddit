from getReddit import getReddit

if __name__ == '__main__':
    print("GETTING TEST POSTS:")
    testPosts = getReddit('askreddit', num_posts=3, comments_per_post=3)
    for post in testPosts:
        post.write_movie()
