import os

from getReddit import getReddit
from image_maker import drawPost
from script_to_speech import script_to_speech
from movie_maker import makeMovie

if __name__ == '__main__':
    print("GETTING TEST POSTS:")
    testPosts = getReddit('askreddit', 3)
    for post in testPosts:
        test_path = os.path.join("./test_resources", post.id)
        os.mkdir(test_path)
        # make images
        print("Generating images...")
        os.mkdir("./test_resources/" + post.id + "/images/")
        drawPost(post.head, post.head.id, 0)
        for i, comment in enumerate(post.comments):
            drawPost(comment, post.id, i+1)
        print("Images created!")
        # create audio
        print("Generating audio...")
        os.mkdir("./test_resources/" + post.id + "/audio/")
        script_to_speech(post, post.id)
        print("Audio created!")
        print("Generating movie...")
        makeMovie(post)
