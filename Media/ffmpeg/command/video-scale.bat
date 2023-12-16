@echo off

rem ffmpeg -i test.mp4 -filter:v scale=1280:720 -c:a copy test-scale.mp4
ffmpeg -i test.mp4 -s 1280x720 -c:a copy test-scale.mp4
rem scale to other size : 640:480, 640x480
pause