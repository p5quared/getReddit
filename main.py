from getReddit import getReddit
from movie_maker import makeMovie

if __name__ == '__main__':
    print("GETTING TEST POSTS:")
    testPosts = getReddit('askreddit', 1)
    for post in testPosts:
        post.dirs_make()

        # make images
        print("Generating images...")
        post.drawPost()
        print("Images created!")

        # create audio
        print("Generating audio...")
        post.script_to_speech()
        print("Audio created!")

        print("Generating movie...")
        makeMovie(post)
        print("Success!! \n Cleaning up...")

        post.dirs_cleanUp()
