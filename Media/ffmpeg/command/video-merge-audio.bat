@echo off

rem merge video with audio (if video has audio will have two sound !!!)
rem ffmpeg -i test.mp4 -i test.mp3 -c:v copy -c:a aac test-merge-audio.mp4

rem replace video audio with new audio 
ffmpeg -i test.mp4 -i test.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 test-replace-audio.mp4

rem loop audio until video finish 
ffmpeg -i a.mp4 -stream_loop -1 -i a.mp3 -map 0:v -map 1:a -c:v copy -shortest ow.mp4