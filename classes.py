import json
import os
import textwrap
from dataclasses import dataclass
from shutil import rmtree

from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS

from movie_maker import make_movie

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
        self.base_working = os.path.join("./working", self.id)
        self.image_dir = os.path.join(self.base_working, 'image/')
        self.sound_dir = os.path.join(self.base_working, 'sound/')
        self.comments = list()

    def write_movie(self):
        self.dirs_make()
        print("Generating images...")
        self.draw_post()
        print("Images created!")
        print("Generating audio...")
        self.script_to_speech()
        print("Audio created!")
        print("Generating movie...")
        make_movie(self, 15)
        print("Success!! \n Cleaning up...")
        self.dirs_clean()

    def script_to_speech(self):
        text_to_convert = [self.head.body] + [comment.body for comment in self.comments]
        for i, text in enumerate(text_to_convert):
            audio_obj = gTTS(text=text, lang="en", slow=False)
            audio_obj.save(self.sound_dir + str(i) + ".mp3")
            #  ie [./test_resources/u1512/audio/{n}.mp3]

    def dirs_make(self):
        if os.path.exists(self.base_working):
            rmtree(self.base_working)
        os.mkdir(self.base_working)
        os.mkdir(self.image_dir)
        os.mkdir(self.sound_dir)

    def dirs_clean(self):
        working_directory = os.path.join("./working", self.id)
        if os.path.exists(working_directory):
            rmtree(working_directory)
        else:
            print(f"ERROR: attempted to delete <{working_directory}> which does not exist.")

    def draw_thumbnail(self):
        title_wrapped = textwrap.wrap(self.head.body, 50)
        title_string = "\n".join(title_wrapped)
        height, width = 1920, 1080

        out = Image.new('RGB', (950, height), color=(0, 0, 0))
        d = ImageDraw.Draw(out)

        font = ImageFont.truetype("Helvetica.ttc", 48)
        d.multiline_text((25, 50), title_string, font=font, fill=(256, 256, 256))
        out.save("./test_resources/test_thumb.jpeg")

    def draw_post(self):
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

            font = ImageFont.truetype(font="~/Library/Fonts/SF-Pro.ttf", size=48)
            d.text((25, 15), poster, font=font, fill=username_color)  # draw username
            d.multiline_text((body_x, 75), body_string, font=font, fill=(0, 0, 0))  # draw comment text
            out.save(self.image_dir + str(i) + ".jpeg")

    def write_test_object(self, i):  # writes post obj to JSON file for quicker testing purposes
        post_object = dict()
        post_object['head'] = self.head.__dict__
        post_object['comments'] = [comment.__dict__ for comment in self.comments]

        with open(f'./test_resources/sample_objects/object_{i}.txt', 'w') as outfile:
            outfile.write(json.dumps(post_object))
