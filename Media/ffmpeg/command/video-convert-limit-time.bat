@ echo off

rem will convert video to 25 second only with format output .avi
rem ffmpeg -i test.mp4 -t 25 test-limit-time.avi


rem will convert video start at time 50 and limit 50 second
ffmpeg -i test.mp4 -ss 00:00:50 -codec copy -t 50 test-limit-start-at.mp4


rem --s - Indicates the starting time of the video clip. In our example, starting time is the 50th second.
rem -t - Indicates the total time duration.

pause