@echo off

ffmpeg -i test.mp3 -af "volume=0.5" test-0.5.mp3

pause