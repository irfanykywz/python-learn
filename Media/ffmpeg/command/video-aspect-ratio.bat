@echo off

ffmpeg -i test.mp4 -aspect 16:9 test-aspect.mp4

rem aspect ratio list :
rem 16:9
rem 4:3
rem 16:10
rem 5:4
rem 2:21:1
rem 2:35:1
rem 2:39:1
pause