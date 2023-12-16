@echo off

rem use file to join
rem ffmpeg -f concat -i video-join.txt -c copy test-join.mp4

rem add -safe 0 if error unsafe file
rem ffmpeg -f concat -safe 0 -i video-join.txt -c copy test-join.mp4

rem directly join
ffmpeg -i "concat:test-part1.mp4|test-part2.mp4" -c copy test-join-direct.mp4
pause