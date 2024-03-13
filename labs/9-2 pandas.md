# BFOR 206 Lab 9-2: Managing data with `pandas`

## Task Description

In this lab, our task is to store relevant YouTube video
metadata in a dataframe and save it to a CSV file.

## Normal Scenario

### Input

**JSON Files:** We will use the JSON data we collected in
the previous lab.

### Output

**File:** A CSV file containing the video metadata.

## Test Cases

### Case 1: Create and save the dataframe

Your script should load the `.json` files that
were saved in the `data/` foler and extract
the following fields:

- `video_id`
- `title`
- `description`
- `length`
- `view_count`

This data should be stored for each video in a dataframe.
The dataframe should be saved to a CSV file in the
`data/` folder with the name `video_metadata.csv`.

## Submission instructions

**Scripts that produce unhandled errors will not be accepted!**

Run your script to show that it produces output that
matches the test cases.

When you are finished, show the instructor:

1. The dataframe with the video metadata for multiple videos.
