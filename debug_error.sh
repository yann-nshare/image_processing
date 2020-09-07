#!/bin/bash

kill -9 $(ps -A | grep python3 | awk '{print $1}')

# use that if you have like error

# [ WARN:0] global /io/opencv/modules/videoio/src/cap_v4l.cpp (887) open VIDEOIO(V4L2:/dev/video0): can't open camera by index
# Traceback (most recent call last):
#   File "test_opencv.py", line 12, in <module>
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# cv2.error: OpenCV(4.2.0) /io/opencv/modules/imgproc/src/color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cvtColor'