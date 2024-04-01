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

    print(f'get_video_metadata: {video_info}')

    return video_info

def ceo_in_title(title: str) -> bool:
    """
    This function will check the title of a video for the 
    keyword "CEO" and return a True/False value if the
    keyword is/is not included.
    """
    
    if 'ceo' in title.lower():
        return True
    else:
        return False

def clean_view_count(view_string: str) -> int:
    pass

def get_video_duration(duration_string: str) -> int:
    """
    This function takes a string of the video duration
    which is normally formatted as MM:SS or HH:MM:SS
    and return the duration as the number of seconds.
    """
    
    # 01:30
    time_parts = duration_string.split(":")
    print(f'time parts {time_parts}')

    # convert the parts to integers and multiply/add
    if len(time_parts) == 2:
        total_seconds = int(time_parts[0]) * 60 + int(time_parts[1])
    else:
        total_seconds = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60 + int(time_parts[2])
    
    print(f'total seconds {total_seconds}')

    return total_seconds

# %% run the video download function
"""
For a description of what this is and how it works, see:
https://stackoverflow.com/questions/419163/what-does-if-name-main-do
"""
if __name__ == '__main__':
    data_dir = 'data'
    get_channel_videos(data_dir)

    # %% find the json files

    json_files = find_json_files(data_dir)

    # %% process json files

    json_data = []
    for file in json_files:
        json_data.append(get_video_metadata(data_dir, file))

    # %% create and save a dataframe

    # create a dataframe with the list of dictionaries
    metadata_df = pd.DataFrame(json_data)

    # %% check for ceo in the title

    # use pandas apply to send data to the ceo_in_title function
    metadata_df['ceo_in_title'] = metadata_df['title'].apply(ceo_in_title)

    # get the duration in seconds
    metadata_df['duration_seconds'] = metadata_df['length'].apply(get_video_duration)

    #%% save it to a CSV file
    metadata_df.to_csv(f'{data_dir}/metadata.csv', index=False)

    # %%
