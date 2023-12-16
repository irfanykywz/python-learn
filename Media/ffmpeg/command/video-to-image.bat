@echo off

ffmpeg -i test.mp4 -r 1 -f image2 image-%2d.png

rem -r - Set the frame rate. I.e the number of frames to be extracted into images per second. The default value is 25.
rem -f - Indicates the output format i.e image format in our case.
rem image-%2d.png - Indicates how we want to name the extracted images. In this case, the names should start like image-01.png, image-02.png, image-03.png and so on. If you use %3d, then the name of images will start like image-001.png, image-002.png and so on.
pause