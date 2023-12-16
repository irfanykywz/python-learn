@echo off

ffmpeg -r 1/10 -i test.png -c:v h264 -r 30 -pix_fmt yuv420p test-image.mp4

rem -r 1/10 : Display each image for 10 seconds.
rem -i test-%01d.png : Reads all tests that starts with name "test-", following with 1 digit (%01d) and ending with .png. If the images name comes with 2 digits (I.e test-10.png, test11.png etc), use (%02d) in the above command.
rem -c:v libx264 : Output video codec (i.e h264).
rem -r 30 : framerate of output video
rem -pix_fmt yuv420p : Output video resolution
rem test.mp4 : Output video file with .mp4 format.
pause