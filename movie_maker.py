from moviepy.editor import *
import os


def makeMovie(post_object):
    # While it might make sense to just past a directory or id instead of the whole object,
    # I feel this is more versatile for future implementations
    base_directory = f'./test_resources/{post_object.id}/'
    audio_directory = base_directory + "audio/"
    image_directory = base_directory + "images/"

    # audio
    audio_clips = []
    for filename in sorted(os.listdir(audio_directory)):
        print(f'Getting audio from {audio_directory + filename}...')
        audio_clips.append((AudioFileClip(audio_directory + filename)))

    joined_audio = concatenate_audioclips(audio_clips)

    # clips
    image_clips = []
    for filename in sorted(os.listdir(image_directory)):
        print(f'Getting image from {image_directory + filename}...')
        image_clips.append(ImageClip(image_directory + filename))
    timed_image_clips = [clip.set_duration(narration.duration) for clip, narration in zip(image_clips, audio_clips)]
    joined_clips = concatenate(timed_image_clips, method="compose")

    # background
    bg = VideoFileClip("./test_resources/ocean_waves_bg.mp4").rotate(90)
    bg_looped = bg.loop(duration=joined_audio.duration)

    # combine
    sub_final = CompositeVideoClip([bg_looped, joined_clips.set_position((65, 600))])
    final = sub_final.set_audio(joined_audio)

    # Audio does not work in quicktime... but it is there. Play in VLC to hear
    final.write_videofile(base_directory + "out.mp3")


if __name__ == '__main__':
    class TestObject:
        def __init__(self, test_id):
            self.id = test_id


    t = TestObject("wxbekm")
    makeMovie(t)
