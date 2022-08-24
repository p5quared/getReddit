from gtts import gTTS


#  Consider using language parameter to translate into other languages
def script_to_speech(post, t_dir, language="en"):
    text_to_convert = [post.head.body] + [comment.body for comment in post.comments]
    for i, text in enumerate(text_to_convert):
        audio_obj = gTTS(text=text, lang=language, slow=False)
        audio_obj.save("./test_resources/" + t_dir + "/" + str(i) + ".mp3")
