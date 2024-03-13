"""
This script will be used to download links and metadata
for YouTube videos from the CNBC YouTube channel.
"""

#%% imports

import os
import pandas as pd
import json
import scrapetube

# %% get the links for the CNBC Channel
def get_channel_videos(data_dir):
    """
    Get the video links for a YouTube channel.
    """
    # get the video links

    channel_url = "https://www.youtube.com/@CNBCtelevision/videos"
    channel_videos = scrapetube.get_channel(channel_url=channel_url, limit=10)

    # this returns a generator object
    print(type(channel_videos))

    # store the json info in files

    # make an empty list to store the information from the generator
    video_list = []
    for video in channel_videos:
        video_list.append(video)
        print(video)

        # write to json file
        data = json.dumps(video)
        
        # name file with video id
        video_id = video['videoId']
        file_name = f'{data_dir}/{video_id}.json'
        with open(file_name, 'w') as f:
            f.write(data)

def find_json_files(data_dir):
    """
    This function will find all of the .json files
    in the data_dir.
    """

    # list the files in the data_dir
    file_list = os.listdir(data_dir)

    # use a loop to check file names 
    json_files = []
    for file in file_list:
        if file.endswith('.json'):
            json_files.append(file)

    # return the list
    return json_files

def get_video_metadata(data_dir, filename):
    """
    This function will load a json file and get 
    the relevant metadata. It will return the data
    in a dictionary. 
    """

    with open(f'{data_dir}/{filename}') as f:
        data = json.load(f)

    # get json data
    video_info = {}
    video_info['video_id'] = data['videoId']
    video_info['title'] = data['title']['runs'][0]['text']
    video_info['description'] = data['descriptionSnippet']['runs'][0]['text']
    video_info['length'] = data['lengthText']['simpleText']
    video_info['view_count'] = data['viewCountText']['simpleText']

    print(f'get_video_info: {video_info}')

# %% run the video download function
data_dir = 'data'
get_channel_videos(data_dir)

# %% find the json files

json_files = find_json_files(data_dir)

# %%
