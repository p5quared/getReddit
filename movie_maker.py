from moviepy.editor import *
from random import randint
import os


def formatBackgroundVideo(target_duration):
    bg = VideoFileClip("./background_clips/minecraft_bg1.mp4") \
        .resize(height=1920) \
        .crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)

    random_in_point = randint(0, int(bg.duration) - (int(target_duration) + 1))
    bg_trimmed = bg.subclip(random_in_point, random_in_point + int(target_duration))
    return bg_trimmed


def makeMovie(post_object):
    base_directory = f'./working/{post_object.id}/'
    audio_directory = base_directory + "sound/"
    image_directory = base_directory + "image/"

    # audio
    audio_clips = []
    for filename in sorted(os.listdir(audio_directory)):
        print(f'Getting audio from {audio_directory + filename}...')
        audio_clips.append((AudioFileClip(audio_directory + filename)))

    joined_audio = concatenate_audioclips(audio_clips)

    # image clips
    image_clips = []
    for filename in sorted(os.listdir(image_directory)):
        print(f'Getting image from {image_directory + filename}...')
        image_clips.append(ImageClip(image_directory + filename))
    timed_image_clips = [clip.set_duration(narration.duration) for clip, narration in zip(image_clips, audio_clips)]
    joined_clips = concatenate(timed_image_clips, method="compose")

    # background
    background_movie = formatBackgroundVideo(joined_clips.duration)

    # combine
    sub_final = CompositeVideoClip([background_movie, joined_clips.set_position((65, 600))])
    final = sub_final.set_audio(joined_audio)

    # Audio does not work in quicktime... but it is there. Play in VLC to hear
    final.write_videofile("./output/" + post_object.id + "_out.mp4")


if __name__ == '__main__':
    test_background = formatBackgroundVideo(5)
    test_background.write_videofile("./output/test_background.mp4")
