@echo off

ffmpeg -i test.mp4 -i test.srt -map 0 -map 1 -c copy -c:s mov_text test-subtitle.mp4

pause