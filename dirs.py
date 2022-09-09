import os


def dirs_make(post):
    working_directory = os.path.join("./working", post.id)
    image = os.path.join(working_directory, 'image')
    sound = os.path.join(working_directory, 'sound')

    if os.path.exists(working_directory):
        os.rmdir(working_directory)

    os.mkdir(working_directory)
    os.mkdir(image)
    os.mkdir(sound)


def dirs_cleanUp(post):
    working_directory = os.path.join("./working", post.id)
    if os.path.exists(working_directory):
        os.rmdir(working_directory)
    else:
        print(f"ERROR: attempted to delete <{working_directory}> which does not exist.")
