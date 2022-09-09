from _dirs import dirs_make, dirs_cleanUp
from _script_to_speech import script_to_speech
from getReddit import getReddit
from image_maker import drawPost
from movie_maker import makeMovie

if __name__ == '__main__':
    print("GETTING TEST POSTS:")
    testPosts = getReddit('askreddit', 1)
    for post in testPosts:
        dirs_make(post)
        # make images
        print("Generating images...")
        drawPost(post.head, post.id, 0)
        for i, comment in enumerate(post.comments):
            drawPost(comment, post.id, i+1)
        print("Images created!")

        # create audio
        print("Generating audio...")

        script_to_speech(post, post.id)
        print("Audio created!")

        print("Generating movie...")
        makeMovie(post)

        print("Success!! \n Cleaning up...")
        dirs_cleanUp(post)
