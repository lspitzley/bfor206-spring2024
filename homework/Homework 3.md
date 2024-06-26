# Homework 3: Video Analysis

The purpose of this homework is to download videos from
YouTube, analyze data from the transcripts, and
use facial recognition to identify people in the videos.

You will learn how to use external libraries to download
and process video data and transcriptions, as well as
how to use facial recognition to identify people in the videos.

To begin the assignment, accept the
[GitHub Classroom assignment](https://classroom.github.com/a/vKwrUZRQ)
and clone the repository to your local machine.

## Tasks

### 1. Transcription Analysis

#### Pre-processing

1. Download the autogenerated transcripts
2. To automate the downloading of many files, you can use the `metadata.csv` file from
    the previous homework to get the video IDs that have CEO in the title. 
    You can load this into a dataframe and use a for loop or apply to get each video ID and
    download the data for that ID. [Example](https://stackoverflow.com/questions/16476924/)
3. Convert the .vtt files to text files. Use `webvtt-py` to convert the files.

#### Analysis

1. Collect at least 100 transcripts (2pts)
2. Tokenize each transcript and get the **total** number of words in each. (1pt)
3. Get the top 50 words from *all* transcripts (2pts)
4. Calculate the positive, negative, and neutral sentiment of the transcripts
    a. Get the average positive, negative, and neutral sentiment for all transcripts (1pt)
    b. Plot the positive, negative, and neutral sentiment in a histogram (1pt)

### 2. Face recognition

#### Pre-processing

1. Download the thumbnails for the videos
2. Use `face_recognition` to identify faces in the thumbnails
3. Save the faces in a `faces` directory
4. To display the images in a notebook, you can use `IPython.display`.
  The import is shown below (you may need to install the package first).
  [Stack Overflow Example](https://stackoverflow.com/questions/11854847/).

```python
from IPython.display import Image, display
```

#### Example

![alt text](displayed_faces.png)

#### Analysis

1. Display the extracted faces in your with the image ID included (2pts)

### 3. Video Analysis

To extract faces from a video, you can adapt the code from this example:
[Extracting faces from videos](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py)

1. Obtain at least 5 videos from the CNBC channel. (1pt)
2. Store the videos in a `videos` directory.
3. Use the faces extracted from the thumbnails to identify people in the videos.
    1. Include a screenshot showing the video with the faces identified (2 pts)
    2. Include a screenshot showing the video with the faces labeled with the video id (or name) (3 pts)

#### Example that meets both 1 & 2:
![alt text](face_id_example.png)

### 4. Deeper Metadata Analysis

#### Pre-processing

The JSON files collected from the video donwload process contain
more information than was available from scraping the channel page.
The process for getting this information is very similar to the process
used to extract the video metadata in the previous homework. You will
instead use the JSON files that are downloaded with yt-dlp.

1. Read the JSON files and select the relevant columns and data points.
2. Store them in a dataframe.
3. Clean any columns that require it.
4. Save the dataframe as a CSV file.
5. Analyze the data in your Jupyter notebook.

#### Analysis

1. Get the average number of comments for the videos (1pt)
2. Get the average number of likes for the videos (1pt)
3. Count the number of vides that were live (1pt)

### 5. Make your results professionally pretty (2 pts)

Use a **Jupyter Notebook** to produce your results. This tool is
easy to use and will produce professional output. They are also
rendered by Github, so you do not need to do any screenshots
or other trickery to make things look nice.

For an example of a notebook, check out this example on
[basic `pandas` functionality](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.03-Operations-in-Pandas.ipynb).

**To receive full credit for your Jupyter Notebook**:

- Use markdown cells to indicate the questions you are answering
- Use markdown cells to describe the results of each section
- Ensure that you have run all of the cells so that the output is visible.
- Do not include code that is not necessary for the analysis (e.g. functions, data cleaning).
  This should be in your `youtube_metadata_download.py` file.
- Do not include any debugging code.
- Do not include any error messages.

### 6. Code Management

1. Have at least 5 commits showing progress. They must be at least an hour apart (spamming 5 commits
   in a row doesn't count!) (2pts)
2. If two people worked on the assignment, then have at least 2 commits per person
  (1pt deduction if not).

## Submission

Submit your code and notebook to the Homework 3 GitHub repository. Make sure that you have
pushed your code to the repository before the deadline. The repository should contain:

1. `download_videos.py`
2. `extract_video_data.py`
3. `homework3.ipynb`
4. (optional) `test_download_videos.py`
5. (optional) `test_extract_video_data.py`

To create your submission repository, click on the following link:
[GitHub Classroom](https://classroom.github.com/a/vKwrUZRQ).

## Grading

There are 22 points available for this homework. The assignment
will be graded out of 15 points. Extra points will count for 
extra credit.

## Due Date

This assignment is due on **May 8th by 11:59pm**.
