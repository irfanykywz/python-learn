@echo off

rem https://ostechnix.com/zoom-in-and-zoom-out-videos-using-ffmpeg/

ffmpeg -i test.mp4 -vf "zoompan=z='if(lte(mod(time,10),3),2,1)':d=1:x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):fps=30" test-zoom.mp4

pause