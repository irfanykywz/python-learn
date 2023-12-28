@echo off

rem ffmpeg -re -stream_loop -1 -i test.mp4 -map 0:v -map 0:a -f flv -ab 128k -acodec aac -ar 44100 -bufsize 5000k -flvflags no_duration_filesize -g 50 -maxrate 2500k -pix_fmt yuv420p -preset veryfast -vb 1000k -vcodec copy -threads 1 rtmp://a.rtmp.youtube.com/live2/123 -hide_banner -progress pipe:1 -y

rem ffmpeg -re -stream_loop -1 -i test2.mp4 -map 0:v -map 0:a -f flv -ab 128k -acodec aac -ar 44100 -bufsize 5000k -flvflags no_duration_filesize -g 50 -maxrate 2500k -pix_fmt yuv420p -preset veryfast -vb 2500k -vcodec libx264 -threads 1 rtmps://live-api-s.facebook.com:443/rtmp/FB-123-0-123

ffmpeg -re -stream_loop -1 -i D:/_APPS/xampp8.0/htdocs/python-learn/Media/ffmpeg/resources/test2.mp4 -f flv -b:v 2500k -b:a 128k -acodec aac -ar 44100 -bufsize 5000k -g 50 -maxrate 2500k -pix_fmt yuv420p -preset veryfast -threads 0 -vcodec libx264 rtmps://live-api-s.facebook.com:443/rtmp/FB-123-0-123 -hide_banner -progress pipe:1 -y


pause