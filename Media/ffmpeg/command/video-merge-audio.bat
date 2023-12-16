@echo off

rem merge video with audio (if video has audio will have two sound !!!)
rem ffmpeg -i test.mp4 -i test.mp3 -c:v copy -c:a aac test-merge-audio.mp4

rem replace video audio with new audio 
ffmpeg -i test.mp4 -i test.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 test-replace-audio.mp4


rem If your audio or video stream is longer, you can add the -shortest option so that ffmpeg will stop encoding once one file ends.
pause