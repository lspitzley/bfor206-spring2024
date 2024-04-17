"""
This script will select videos from a 
pre-made list of video IDs (CNBC video metadata).

It will download the videos, the transcripts,  
the highest-quality thumbnail, and video-specific
metadata. 
"""

#%% imports

import yt_dlp


#%% options

# place to save videos
output_folder = 'data/videos/'

# yt-dlp options
vid_opts = {
    'format': 'bestvideo+bestaudio/best',
	'outtmpl': f'{output_folder}%(id)s.%(ext)s',
	'writeinfojson': True,
}
#%% functions

def get_video_ids():
    pass

def get_metadata(video_id):
    pass

def get_transcripts(video_id):
    pass

def get_thumbnails(video_id):
    pass

def download_video(video_id):
    """
    This function uses the yt-dlp package to download
    the video with the given video_id.
    """
    vid_ydl = yt_dlp.YoutubeDL(vid_opts)
    vid_ydl.download([video_id])

    

#%% main

if __name__ == '__main__':
    video_id = 'ernwEzDFGu8'
    print(f'Downloading video {video_id}')
    download_video(video_id)


# %%
