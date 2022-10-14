# getReddit
A script that turns any text based post from Reddit into a Youtube clip with narration and background video.

## Before Use:
1. Clone Repository 
```shell
git clone https://github.com/p5quared/getReddit
```
2. Modify User Credentials to Your Own in these Locations:
```python
# getReddit
client_id=environ['CLIENT_ID'],
client_secret=environ['CLIENT_SECRET'],

# upload_manager.py
channel.login("./credentials/yt_client_secret.json",
              "./credentials/credentials.storage")
```
You will need to get credentials to use the Youtube Data API in order to upload via Python.

3. Download a background video file and place in location referenced here:
```python
# movie_maker.py
bg = VideoFileClip("./background_clips/minecraft_bg1.mp4") \
```


Resulting video(s) will be saved to the folder called 'output' with the format '{reddit_post.id}.mp3'
