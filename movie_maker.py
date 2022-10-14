from random import randint

from moviepy.editor import *
from moviepy.video.VideoClip import ImageClip


# noinspection PyUnresolvedReferences,GrazieInspection
def format_background_video(target_duration):
    """
    Mutates a 1920x1080 movie to be 1080x1920, and trims it to a desired length.

    :param target_duration:
    :return:  moviepy.VideoFileClip
    """
    bg = VideoFileClip("./background_clips/minecraft_bg1.mp4") \
        .resize(height=1920) \
        .crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)

    random_in_point = randint(0, int(bg.duration) - (int(target_duration) + 1))
    bg_trimmed = bg.subclip(random_in_point, random_in_point + target_duration)
    return bg_trimmed


def manage_size(post_object, audio_clips, img_clips, desired_length):
    """
     When single movies are too long, splits movie up and returns list of movies.

    :param post_object:
    :param audio_clips:
    :param img_clips:
    :param desired_length:
    :return :  list(dict(movie_attr))
    """
    temp_audio = list()
    temp_clips = list()
    desired_movies = list(dict())  # [{name:'id_x', audio:'y' clips:'z', bg:'bg'},{}...]
    for i, (audio_clip, img_clip) in enumerate(zip(audio_clips[1:], img_clips[1:])):  # first clip is title
        if len(temp_audio) == 0 or audio_clips[0].duration + sum(
                [clip.duration for clip in temp_audio]) < desired_length:
            temp_audio.append(audio_clip)
            temp_clips.append(img_clip)
        else:
            movie = dict()
            movie['name'] = post_object.id + '_' + str(i)
            movie['audio'] = concatenate_audioclips([audio_clips[0]] + temp_audio)
            movie['clips'] = concatenate_videoclips([img_clips[0]] + temp_clips)
            movie['bg'] = format_background_video(movie['audio'].duration)
            desired_movies.append(movie)
            temp_audio = list()
            temp_clips = list()
    print(f'Generated {len(desired_movies)} unique movies!')
    return desired_movies


def compile_movie(movie):
    """
    Renders movie from movie dict() object.

    :param movie:
    :return: .mp4
    """
    movie_out = CompositeVideoClip([movie['bg'], movie['clips'].set_position((65, 600))]).set_audio(movie['audio'])
    movie_out.write_videofile("./output/" + movie['name'] + ".mp4")


def make_movie(post_object, desired_length: int):
    """
    Main driver for movie process.
    Organizes video and audio clips and calls appropriate helper functions.

    :param post_object:
    :param desired_length:
    :return:
    """
    audio_clips: list[AudioFileClip] = []
    for filename in sorted(os.listdir(post_object.sound_dir)):
        audio_clips.append((AudioFileClip(post_object.sound_dir + filename)))

    image_clips: list[ImageClip] = []
    for filename in sorted(os.listdir(post_object.image_dir)):
        image_clips.append(ImageClip(post_object.image_dir + filename))
    timed_image_clips = [clip.set_duration(narration.duration) for clip, narration in zip(image_clips, audio_clips)]

    desired_movies = manage_size(post_object, audio_clips, timed_image_clips,
                                 desired_length)  # {output_name: [ints corresponding to clips to use]}

    for movie in desired_movies:
        compile_movie(movie)


if __name__ == '__main__':
    test_background = format_background_video(5)
    test_background.write_videofile("./output/test_background.mp4")
