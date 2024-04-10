# Homework 2: Data Cleaning and Analysis

The purpose of this homework is analyze the metadata
from the YouTube videos on the CNBC channel. The repository
for this assignment is located at:
[Github Classrooom](https://classroom.github.com/a/x-3aL8Jp).
You may work with one other person on this homework.

## Tasks

There will be three files that you will need to use for this assignment.

1. `youtube_metadata_download.py` - This file will download the metadata for the videos
2. `test_youtube_metadata_download.py` - This file will test the functions in the first file
3. `homework2.ipynb` - This file will contain the analysis of the data

### 1. Get video metadata

1. Obtain metadata for at least 1000 videos. (1pt)
2. Store the metadata in a `csv` file. (1pt)
3. The metadata should include *at least* the following fields: (1pt)
   - `video_id`
   - `title`
   - `description`
   - `views`
   - `duration`

### 2. Summarize data

1. How many videos have the keyword "CEO" in the title? (1pt)
2. What is the average number of views for all videos? (1pt)
3. What is the average number of views for videos with "CEO" in the title? (1pt)
4. How long is the average video? (1pt)
5. How long is the average video with "CEO" in the title? (1pt)
6. What are the longest and shortest videos? Include the video title and duration in your output. (1pt)

### 3. Visualizations

1. Create a histogram of the number of views for all videos. Are there any outliers? (1pt)
2. Create a histogram of the number of views for videos with "CEO" in the title. Are there any outliers? (1pt)
3. Create a histogram of the duration of all videos. Are there any outliers? (1pt)
4. Create a histogram of the duration of videos with "CEO" in the title. Are there any outliers? (1pt)

### 4. Deeper analysis

1. What are the 100 most common words in the video titles? What do you find interesting about this list? (1pt)
2. What are the most common words in the video descriptions? How does it compare to the video titles? (1pt)

### 5. Code Management

1. Have at least 5 commits showing progress. They must be at least an hour apart (spamming 5 commits
   in a row doesn't count!) (2pts)
2. If two people worked on the assignment, then have at least 2 commits per person
  (1pt deduction if not).

### 6. Make your results professionally pretty (2 pts)

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
- Do not include any debugging code or print statements.
- Do not include any error messages.

### 6. Testing

1. Write tests for the functions in `youtube_metadata_download.py`.
    1. Test for `ceo_in_title` (1pt)
    2. Test for `clean_view_count` (1pt)
    3. Test for `clean_duration` (1pt)

You will receive 1 point for each test that passes.

## Submission

Submit your code and notebook to the Homework 2 GitHub repository. Make sure that you have
pushed your code to the repository before the deadline. The repository should contain:

1. `youtube_metadata_download.py`
2. `test_youtube_metadata_download.py`
3. `homework2.ipynb`

To create your submission repository, click on the following link:
[Github Classroom](https://classroom.github.com/a/x-3aL8Jp).

## Grading

There are 22 points available for this homework. The assignment
will be graded out of 18 points. The maximum grade for this
is 22/18. The remaining 4 points will be used as extra credit.

## Due Date

This assignment is due on **April 21st by 11:59pm**.
