from PIL import Image, ImageDraw, ImageFont
import textwrap

username_color = (0, 0, 0)
bg_color = (245, 245, 245)


def drawPost(post_object, _id: str, i: int):
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
    if post_object.isReply:  # pushes body over and adds reply line
        d.line((10, 120, 10, out.size[1] * .9), fill=(85, 89, 92), width=4)
        body_x = + 25
        poster = "Reply by: " + poster.authorName

    font = ImageFont.truetype("Helvetica.ttc", 48)
    d.text((25, 50), poster, font=font, fill=username_color)  # draw username
    d.multiline_text((body_x, 120), body_string, font=font, fill=(0, 0, 0))  # draw comment text
    out.save("./test_resources/" + _id + "/images/" + str(i) + ".jpeg")
    if __name__ == '__main__':
        out.save("./test_resources/" + post_object.authorName + ".jpeg")


#  Optimizing for mobile/tiktok size (1080x1920)
if __name__ == '__main__':
    class SampleObject:
        def __init__(self, body: str, is_submission=False, is_reply=False):
            self.body = body
            self.authorName = "someUser" + '12351235'
            self.isSubmission = is_submission
            self.isReply = is_reply
            self.score = 2_200
            self.id = 'steadfastness'


    fake_comment = SampleObject(
        "It's a small migratory bird, a delicacy in French cuisine. They're caught with nets, locked in a cage so they gorge themselves on grain until they're fat, then they're drowned in cognac to marinate the meat, and cooked and eaten whole. The traditional way of eating them is while covering your head with a towel so God doesn't see the indulgent and depraved thing you're doing, so that says something.")
    fake_comment2 = SampleObject(
        "This is another users comment. Obviously this is not really a top comment on a Reddit post, but it is something with words an such and will serve for testing purposes.",
        is_reply=False)
    fake_submission = SampleObject("Meat eaters: what type of meat, if any, is off your menu for ethical reasons?",
                                   is_submission=True)

    drawPost(fake_comment, 0)
    #    drawPost(fake_comment2)
    drawPost(fake_submission, 1)
