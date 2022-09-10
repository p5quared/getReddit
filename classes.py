from dataclasses import dataclass
from gtts import gTTS
import os
from shutil import rmtree
from PIL import Image, ImageDraw, ImageFont
import textwrap

username_color = (0, 0, 0)
bg_color = (245, 245, 245)


@dataclass(frozen=True, order=True)
class RedditObject:
    score: int
    id: int
    authorName: str
    subreddit: str
    body: str
    isSubmission: bool = False
    isReply: bool = False


class Post:
    head: RedditObject
    comments: [RedditObject]
    isMovie: bool = False

    def __init__(self, head):
        self.head = head
        self.id = head.id
        self.comments = list()

    def script_to_speech(self):
        text_to_convert = [self.head.body] + [comment.body for comment in self.comments]
        for i, text in enumerate(text_to_convert):
            audio_obj = gTTS(text=text, lang="en", slow=False)
            audio_obj.save("./working/" + self.id + "/sound/" + str(i) + ".mp3")
            #  ie [./test_resources/u1512/audio/{n}.mp3]

    def dirs_make(self):
        working_directory = os.path.join("./working", self.id)
        image = os.path.join(working_directory, 'image')
        sound = os.path.join(working_directory, 'sound')
        if os.path.exists(working_directory):
            rmtree(working_directory)
        os.mkdir(working_directory)
        os.mkdir(image)
        os.mkdir(sound)

    def dirs_cleanUp(self):
        working_directory = os.path.join("./working", self.id)
        if os.path.exists(working_directory):
            rmtree(working_directory)
        else:
            print(f"ERROR: attempted to delete <{working_directory}> which does not exist.")

    def drawPost(self):
        for i, post_object in enumerate([self.head] + self.comments):
            body_wrapped = textwrap.wrap(post_object.body, 40)  # 2nd arg is a width limiter
            body_string = "\n".join(body_wrapped)

            # size canvas
            if len(body_wrapped) == 1:
                height = 48 * 4  # this just works out in my samples for one line comments
            else:
                height = (len(body_wrapped) + 3) * 48  # roughly height of wrapped-text plus 2 lines

            # Pillow Stuff
            out = Image.new('RGB', (950, height), color=bg_color)
            d = ImageDraw.Draw(out)

            poster = "u/" + post_object.authorName + ":"
            if post_object.isSubmission:
                poster = "Posted by: " + poster
            body_x = 25
            # if post_object.isReply:  # pushes body over and adds reply line
            #     d.line((10, 120, 10, out.size[1] * .9), fill=(85, 89, 92), width=4)
            #     body_x = + 25
            #     poster = "Reply by: " + poster.authorName

            font = ImageFont.truetype("Helvetica.ttc", 48)
            d.text((25, 50), poster, font=font, fill=username_color)  # draw username
            d.multiline_text((body_x, 120), body_string, font=font, fill=(0, 0, 0))  # draw comment text
            out.save("./working/" + self.id + "/image/" + str(i) + ".jpeg")
