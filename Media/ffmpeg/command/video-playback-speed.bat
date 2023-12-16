@echo off

rem increse video playback
ffmpeg -i test.mp4 -vf "setpts=0.5*PTS" test-playback-pts.mp4

rem increse audio playback
rem ffmpeg -i test.mp4 -filter:a "atempo=2.0" test-playback-speed.mp4

rem if you want result without video use -vn
rem ffmpeg -i test.mp4 -filter:a "atempo=2.0" -vn test-playback-speed.mp4

pause