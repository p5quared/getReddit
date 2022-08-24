import os

from getReddit import getReddit
from image_maker import drawPost
from script_to_speech import script_to_speech

if __name__ == '__main__':
    print("GETTING TEST POSTS:")
    testPosts = getReddit('askreddit', 3)
    one_test = testPosts[0]
    test_path = os.path.join("./test_resources", one_test.id)
    # make images
    print("Generating images...")
    drawPost(one_test.head, one_test.head.id, 0)
    for i, post in enumerate(one_test.comments):
        drawPost(post, one_test.head.id, i+1)
    print("Images created!")
    # create audio
    print("Generating audio...")
    script_to_speech(one_test, one_test.head.id)
    print("Audio created!")
