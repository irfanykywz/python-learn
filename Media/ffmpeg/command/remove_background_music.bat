@echo off
rem ffmpeg -i test.mp4 -af "volume=0,asetpts=N/SR/TB" -c:v copy -c:a aac -strict experimental -b:a 192k test_rm.mp4
rem ffmpeg -i test.mp3 -af "afftdn=nr=1:nf=-20:tn=0" test_rm.mp3

rem ffmpeg -i "test.mp3" -vn -ac 2 -ar 44100 -ab 320k -f mp3 test_rm.mp3

ffmpeg -i je.mp4 -vn je.mp3


rem https://stackoverflow.com/questions/75521143/isolating-separating-vocals-from-audio-by-ffmpeg
rem ffmpeg -i lil.wav -af pan="stereo|c0=c0|c1=-1*c1" -ac 1 lil_rm.mp3

rem ffmpeg -i test.mp3 -af afftdn test_rm.mp3
pause

rem FFMpeg Commands:
rem extract audio:
rem ffmpeg -i input.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 output.wav

rem combine 1 audio track:
rem ffmpeg -i "video.mp4" -i "audio.wav" -c:v copy -c:a aac "output.mp4"

rem combine 2 audio tracks:
rem ffmpeg -i "input_video.avi" -i "track_1.wav" -i "track_2.wav" -map 0:v -map 1:a -map 2:a -c:v copy "output_file.mp4"

