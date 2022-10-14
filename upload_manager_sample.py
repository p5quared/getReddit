#!/usr/bin/python
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

# log into the channel
channel = Channel()
channel.login("./credentials/yt_client_secret.json", "./credentials/credentials.storage")

# setting up the video that is going to be uploaded
video = LocalVideo(file_path="./test_resources/test_vid1.mp4")

# setting snippet
video.set_title("test_upload")
video.set_description("This is a description")
video.set_tags(["sample", "tag"])
video.set_category("entertainment")
video.set_default_language("en-US")

# setting status
video.set_embeddable(True)
video.set_license("creativeCommon")
video.set_privacy_status("private")
video.set_public_stats_viewable(True)

# setting thumbnail
# video.set_thumbnail_path('test_thumb.png')

# uploading video and printing the results
video = channel.upload_video(video)
print(video.id)
print(video)

# liking video
video.like()
