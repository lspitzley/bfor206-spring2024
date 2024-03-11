"""
This script will be used to download links and metadata
for YouTube videos from the CNBC YouTube channel.
"""

#%% imports

import pandas as pd
import json
import scrapetube

# %% get the links for the CNBC Channel

channel_url = "https://www.youtube.com/@CNBCtelevision/videos"
channel_videos = scrapetube.get_channel(channel_url=channel_url, limit=10)

# this returns a generator object
print(type(channel_videos))

# %% store the json info in files

# make an empty list to store the information from the generator
video_list = []
for video in channel_videos:
    video_list.append(video)
    print(video)

    # write to json file
    data = json.dumps(video)
    
    # name file with video id
    video_id = video['videoId']
    file_name = f'data/{video_id}.json'
    with open(file_name, 'w') as f:
        f.write(data)


# %%
