@echo off

ffmpeg -i test.mp4 -i test.png -map 0 -map 1 -c copy -c:v:1 png -disposition:v:1 attached_pic test_thumbnail.mp4

pause