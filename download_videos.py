"""
This script will select videos from a 
pre-made list of video IDs (CNBC video metadata).

It will download the videos, the transcripts,  
the highest-quality thumbnail, and video-specific
metadata. 
"""

#%% imports

import os
import yt_dlp


#%% options

# place to save videos
video_folder = 'data/videos/'
transcript_folder = 'data/transcripts/'

# yt-dlp options
vid_opts = {
    'format': 'bestvideo+bestaudio/best',
	'outtmpl': f'{video_folder}%(id)s.%(ext)s',
	'writeinfojson': True,
}

transcript_opts = {
	'skip_download': True,
	'writeautomaticsub': True,
	'subtitleslangs': ['en'],
	'subtitlesformat': 'vtt',
	'outtmpl': f'{transcript_folder}%(id)s.%(ext)s',
	'writeinfojson': False,
}

#%% functions

def get_video_ids():
    pass

def get_metadata(video_id):
    pass

def get_transcripts(video_id):
    """
    This function downloads the transcript for 
    the given video_id.
    """
    ts_ydl = yt_dlp.YoutubeDL(transcript_opts)
    ts_ydl.download([video_id])

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

    # check if the video has already been downloaded
    if os.path.exists(f'{video_folder}{video_id}.webm'):
        print(f'Already downloaded video {video_id}. Skipping...')
    else:
        print(f'Downloading video {video_id}')
        download_video(video_id)


# %%
