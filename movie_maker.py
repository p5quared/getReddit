from moviepy.editor import *

if __name__ == '__main__':
    title = AudioFileClip("./test_resources/title_audio.mp3")
    com1 = AudioFileClip("./test_resources/comment1.mp3")
    com2 = AudioFileClip("./test_resources/comment2.mp3")

    joined_audio = concatenate_audioclips([title, com1, com2])

    bg = VideoFileClip("./test_resources/ocean_waves_bg.mp4").rotate(90)
    bg_looped = bg.loop(duration=joined_audio.duration)
    title_im = ImageClip("./test_resources/title_im.jpeg").set_duration(title.duration)
    com1_im = ImageClip("./test_resources/com1.jpeg").set_duration(com1.duration)
    com2_im = ImageClip("./test_resources/com2.jpeg").set_duration(com2.duration)

    reddit_clips = concatenate([title_im, com1_im, com2_im], method="compose")
    sub_final = CompositeVideoClip([bg_looped, reddit_clips.set_position((65, 600))])
    final = sub_final.set_audio(joined_audio)

    final.write_videofile("./test_resources/output.mp4")

'''
width of frame =      1080px
width of text images = 950px
adjusted x =           130px
1920
960

get length of audio clips
[Title = 5s], [C1 = 9s], [C2 = 11s]
>concatenate

run background clip for duration of audio

show images at correct timestamps...
[Ti = 0>>5s], [C1i = 5s >> 9s], [C2i = 9s >> 20s]

join it all


NOTE>> Use compositeVideoClip to just slap replies on top of comments
'''
