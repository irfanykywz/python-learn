@echo off

rem ffmpeg -i test.mp4 test.avi
rem ffmpeg -i test.mp4 test.mpeg

rem convert with keep quality 
rem ffmpeg -i test.mp4 -qscale 0 test-cv.avi

rem check list format available
ffmpeg -formats

pause