# TODO --> USE PIL to generate images
#           (background, user, body)
#           maybe figure out solutions for [comment] threads
from PIL import Image, ImageDraw, ImageFont
import textwrap

#  Optimizing for mobile/tiktok size (1080x1920)
if __name__ == '__main__':
    class SampleObject:
        def __init__(self):
            self.body = "It's a small migratory bird, a delicacy in French cuisine. They're caught with nets, locked in a cage so they gorge themselves on grain until they're fat, then they're drowned in cognac to marinate the meat, and cooked and eaten whole. The traditional way of eating them is while covering your head with a towel so God doesn't see the indulgent and depraved thing you're doing, so that says something."
            self.name = "/u/UnoriginalUse"
            self.isReply = False
            self.score = 2_200
    fake_post = SampleObject()

    lines = textwrap.wrap("What the fuck. Fucking gross.", 40)
    dString = "\n".join(lines)

    # Get desired canvas height
    if len(lines) == 1:
        height = 48 * 4
    else:
        height = (len(lines) + 2) * 48

    out = Image.new('RGB', (1080, height), color=(0, 0, 0))
    d = ImageDraw.Draw(out)

    font = ImageFont.truetype("Helvetica.ttc", 48)
    d.text((90, 50), "u/someuser:", font=font, fill=(256, 256, 256))  # draw title
    d.multiline_text((90, 120), dString, font=font, fill=(256, 256, 256))  # draw comment

    out.show()
