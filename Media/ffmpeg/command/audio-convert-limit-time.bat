@echo off

ffmpeg -i test.mp3 -ss 00:00:50 -to 00:01:30 -c copy test-limit-start-at.mp3

pause