@echo off

rem ffmpeg -i test.mp4 -vn test.mp3


rem audio transcoding output
ffmpeg -i test.mp4 -vn -ar 44100 -ac 2 -ab 320k -f mp3 test.mp3

rem -vn - Indicates that we have disabled video recording in the output file.
rem -ar - Set the audio frequency of the output file. The common values used are  22050, 44100, 48000 Hz.
rem -ac - Set the number of audio channels.
rem -ab - Indicates the audio bitrate.
rem -f - Output file format. In our case, it's mp3 format.

pause