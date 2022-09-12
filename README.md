# getReddit
A script that turns any text based (for now) post from Reddit into a youtube shorts clip with narration and background video.

##How to use:
1. Clone repository 
git clone https://github.com/p5quared/getReddit
2. In 'getReddit.py', edit the pRAW elements to reflect your own client_id and client_secret tokens.
3. Download an appropriate background video. The one I used is located [here]. Place it in the root directory and rename it to background.mp4.
4. Run from your favorite IDE or terminal (python main.py)

Resulting video(s) will be saved to the folder called 'output' with the format '{reddit_post.id}.mp3'
