@echo off

rem download 20 video on playlist
rem yt-dlp --playlist-items 20 https://www.youtube.com/playlist?list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB

rem convert to another format
rem yt-dlp --playlist-items 1 -x --audio-format mp3 https://www.youtube.com/playlist?list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB

rem download random by position video
rem yt-dlp --playlist-items 2,3,7,10 https://www.youtube.com/playlist?list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB

rem download start at position and end with postition
rem yt-dlp --playlist-start 10 --playlist-end 5 https://www.youtube.com/playlist?list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB

