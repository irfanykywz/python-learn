@echo off

ffmpeg -i test.mp4 -t 00:00:30 -c copy test-part1.mp4 -ss 00:00:30 -codec copy test-part2.mp4

pause