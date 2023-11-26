# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 22:43:45 2023

@author: dekom
"""
import cv2
import os
import tqdm
# Parameters
folder_path = 'history'
output = 'output_video.avi'
frame_rate = 30  # frames per second
size = (1920, 1080)  # video size

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter(output, fourcc, frame_rate, size)

# Retrieve all PNG files and their creation times
files_with_ctime = [(file, os.path.getctime(os.path.join(folder_path, file)))
                    for file in os.listdir(folder_path)
                    if file.endswith('.png')]

# Sort files by creation time
sorted_files = [file for file, _ in sorted(files_with_ctime, key=lambda x: x[1])]

# Write each sorted file to the video
for file in tqdm(sorted_files):
    image_path = os.path.join(folder_path, file)
    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, size)  # Resize frame
    video_writer.write(frame)  # Write frame to video

# Release the video writer
video_writer.release()

print('finished')