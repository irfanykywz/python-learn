
@echo off
ffmpeg -ss 1 -i test.mp4 -vframes 1 -y "test.png"
pause