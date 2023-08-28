import cv2 as cv
import numpy as np
import datetime
import os

# Open the webcam
capturer = cv.VideoCapture(1)

beginning_timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_folder = r'C:\Users\wwwsh\Videos\Training Data'
output_filename = os.path.join(output_folder, f'{beginning_timestamp}.mp4')

# Define the codec and create a VideoWriter object to save the video
fourcc = cv.VideoWriter_fourcc(*'X264')
fps = 30
frame_size = (1920, 1080)  # My webcam resolution is 1080p
out = cv.VideoWriter(output_filename, fourcc, fps, frame_size)

while capturer.isOpened():
    ret, frame = capturer.read()
    if not ret:
        break

    # Add timestamp to the frame
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cv.putText(frame, timestamp, (10, frame.shape[0] - 10),
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    out.write(frame)  # Write the frame with timestamp to the video

    cv.imshow('Webcam with Timestamp', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capturer.release()
out.release()
cv.destroyAllWindows()