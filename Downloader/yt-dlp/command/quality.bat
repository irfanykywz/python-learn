@echo off
rem yt-dlp -f worstvideo https://www.youtube.com/watch?v=QmjrLljcYSw

rem merge video + audio
rem yt-dlp -f worstvideo+bestaudio https://www.youtube.com/watch?v=QmjrLljcYSw

rem separate video & audio command :
rem yt-dlp -f 'worstvideo,bestaudio' https://www.youtube.com/watch?v=QmjrLljcYSw

rem download with specifict resuliton < 360 pixel = 360p
rem yt-dlp -f "best[height<=360]" https://www.youtube.com/watch?v=QmjrLljcYSw

rem download with format id
rem yt-dlp -f 247 https://www.youtube.com/watch?v=t5b20oLaIaw

rem download with format id use expression > ex if id 22 not exist use id 17, if 17 not exist use 18
rem yt-dlp -f 22/17/18 https://www.youtube.com/watch?v=t5b20oLaIaw

rem download with custom output
yt-dlp -f mp4 https://www.youtube.com/watch?v=QmjrLljcYSw -o '%(title)s.f%(format_id)s.%(ext)s'

rem merge video + audio with specifict resolution
rem yt-dlp -f 'bestvideo[height<=480]+bestaudio/best[height<=480]' https://www.youtube.com/watch?v=QmjrLljcYSw

rem best (b): This selects the highest quality format available, including both video and audio.
rem worst (w): It picks the lowest quality format for both video and audio.
rem bestvideo (bv): This option selects the best quality video-only format (e.g., DASH video).
rem worstvideo (wv): Similar to bestvideo but chooses the lowest quality video-only format.
rem bestaudio (ba): This selects the best quality audio-only format.
rem worstaudio (wa): Similar to bestaudio but chooses the lowest quality audio-only format.
pause