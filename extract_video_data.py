"""
This script will process data from transcripts,
thumbnails, and videos
"""

#%% imports

import os
import webvtt
import cv2


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

def detect_faces(video_id, thumbnail_folder, faces_folder):
    """
    This function uses openCV to find faces in a thumbnail
    image and saves the extracted face to the `faces` folder.
    """

    img = cv2.imread(f'{thumbnail_folder}{video_id}.jpg')
    print(f'image loaded, with shape: {img.shape}')

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # load face classifier
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces = face_classifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(40,40))

    print(faces)

    # write to a file
    count = 0
    for (x,y,w,h) in faces:
        face = img[y:y+h, x:x+w] #slice the face from the image
        cv2.imwrite(f'{faces_folder}{video_id}-{str(count)}.jpg', face) #save the image
        count+=1




#%% main

if __name__ == '__main__':
    transcript_folder = 'data/transcripts/'
    thumbnail_folder = 'data/thumbnails/'
    faces_folder = 'data/faces/'


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


    # extract faces
    detect_faces(video_id, thumbnail_folder, faces_folder)


# %%
