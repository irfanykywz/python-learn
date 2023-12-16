@echo off

rem basic command :
rem ffmpeg -i test.mp4 -filter:v "crop=w:h:x:y" test-crop.mp4

rem use:
ffmpeg -i test.mp4 -filter:v "crop=320:320:100:100" test-crop.mp4


rem test.mp4 - source video file.
rem -filter:v - Indicates the video filter.
rem crop - Indicates crop filter.
rem w - Width of the rectangle that we want to crop from the source video.
rem h - Height of the rectangle.
rem x - x coordinate of the rectangle that we want to crop from the source video.
rem y - y coordinate of the rectangle.

pause