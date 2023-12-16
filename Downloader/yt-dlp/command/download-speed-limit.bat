@echo off

rem limit 50KB/s
yt-dlp -r 50K https://www.youtube.com/watch?v=QmjrLljcYSw

rem continue downloading
yt-dlp -c https://www.youtube.com/watch?v=QmjrLljcYSw