"""
This script will process data from transcripts,
thumbnails, and videos
"""

#%% imports

import os
import webvtt


# %% functions

def clean_transcript(captions):
    """
    This function takes a webvtt list of captions
    and converts them to a single string of text.
    """

    full_text = ''
    for caption in captions:
        caption.text = caption.text.split('\n')[-1]
        full_text += caption.text
    
    return full_text

def detect_faces():
    pass

#%% main

if __name__ == '__main__':
    transcript_folder = 'data/transcripts/'


    # example video id
    video_id = 'ernwEzDFGu8'

    # load the trancsript
    captions = webvtt.read(f'{transcript_folder}{video_id}.en.vtt')
    print(f'Caption 0: {captions[0]}')
    print(f'Caption 0 text: {captions[0].text}')


    text = clean_transcript(captions)
    print(text)

    with open(f'{transcript_folder}{video_id}.txt', 'w') as f:
        f.write(text)

# %%
