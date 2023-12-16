@echo off

ffmpeg -i test.mp3 -ab 128 test-compress.mp3

rem audio bitrate :
rem 96kbps
rem 112kbps
rem 128kbps
rem 160kbps
rem 192kbps
rem 256kbps
rem 320kbps
pause