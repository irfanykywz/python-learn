@echo off

rem https://www.blackhatworld.com/seo/how-bypass-100-copyright-youtube.1481507/

rem hasilnya gepeng
rem ffmpeg -i test.mp4 -vf "zoompan=z='if(lte(mod(time,10),3),2,1)':d=1:x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):fps=29.97" test-zoom-bypass.mp4

rem ffmpeg -i test.mp4 -vf "zoompan=z='if(lte(mod(time,10),3),2,1)':d=1:x=iw/3.5-(iw/zoom/3.5)+50:y=ih/3.5-(ih/zoom/3.5)-40:fps=29.97" -an test-zoom-bypass2.mp4

rem ffmpeg -i test.mp4 -vf "zoompan=z='if(lte(mod(time,10),4),2,1)':d=1:x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):fps=29.97" test-zoom-bypass3.mp4

ffmpeg -i test.mp4 -filter:a "highpass=f=1375.4,volume=12.3dB" audio_result.mp4