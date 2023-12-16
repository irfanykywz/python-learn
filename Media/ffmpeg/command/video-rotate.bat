@echo off

rem https://ostechnix.com/how-to-rotate-videos-using-ffmpeg-from-commandline/

rem ffmpeg -i test.mp4 -vf "transpose=1" test-rotate.mp4
rem transpose=clock

rem rotate include metadata
ffmpeg -i test.mp4 -map_metadata 0 -metadata:s:v rotate="90" -codec copy test-rotate-metadata.mp4

rem list of available parameters for transpose feature.
rem 0 - Rotate by 90 degrees counter-clockwise and flip vertically. This is the default.
rem 1 - Rotate by 90 degrees clockwise.
rem 2 - Rotate by 90 degrees counter-clockwise.
rem 3 - Rotate by 90 degrees clockwise and flip vertically.

pause