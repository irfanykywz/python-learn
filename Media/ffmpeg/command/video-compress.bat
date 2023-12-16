@echo off

ffmpeg -i test.mp4 -vf scale=1280:-1 -c:v libx264 -preset veryslow -crf 24 test-compress.mp4
rem down audio to : -ac 2 -c:a aac -strict -2 -b:a 128k
pause