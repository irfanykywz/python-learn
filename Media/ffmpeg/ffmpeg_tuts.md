Extract audio from a YouTube video file

```sh
ffmpeg -i INPUT.mp4 -ab 256k OUTPUT.mp3
```

Cut 3s length

```sh
ffmpeg -y -ss 00:00:03 -i INPUT.mp4 -codec copy OUTPUT.mp4
```

Cut 30s length after first 3s

```sh
ffmpeg -y -ss 00:00:03 -i INPUT.mp4 -to 00:00:30 -codec copy OUTPUT.mp4
```

Clear ID3 Tag Metadata

```sh
ffmpeg -y -i INPUT.mp4 -codec copy -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -preset superfast OUTPUT.mp4
```

Cut 3s, change MD5 Hash, clear ID3 Tag Metadata

```ssh
ffmpeg -y -ss 00:00:03 -i input.mp4 -codec copy output_cut.mp4

ffmpeg -y -i output_cut.mp4 -codec copy -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -preset superfast output.mp4

delete output_cut.mp4
```

Crop and Resize

```sh
ffmpeg -y -i input.mp4 -filter_complex "crop=640:360:10:10,scale=320:240,setdar=16/9" output.mp4
```

Vignette

```sh
//vignette=0-10
ffmpeg -y -i input.mp4 -filter_complex "vignette=5" output.mp4
```

Zoom

```sh
//zoom 150% to center
ffmpeg -y -i input.mp4 -filter_complex "crop=iw/2:ih/2,scale=640:360" output.mp4

//zoom 150% from left top corner
//ffmpeg -y -i input.mp4 -filter_complex "crop=iw/2:ih/2:0:0,scale=640:360" output.mp4
```

Extract a frame as image

```sh
//Extract a frame at 30s
ffmpeg -y -i input.mp4 -ss 00:00:30 -frames:v 1 output.mp4
```

Create Thumbnail every 10 seconds

```sh
ffmpeg -y -i imput.mp4 -f image2 -vf "fps=1/10" output.mp4
```

Speed up video and audio

```sh
//Speed up to 170% = 1.7
ffmpeg -y -i input.mp4 -filter_complex "setpts=PTS/1.7; atempo=1.7" output.mp4
```

Overlay Logo or Filter

```sh
//Overlay Logo
ffmpeg -y -i input.mp4 -i "Logo.png" -filter_complex "[0:v][1:v]overlay=10:10" output.mp4
//Overlay Filter
//ffmpeg -y -i input.mp4 -i "Filter.png" -filter_complex "[0:v][1:v]overlay=0:0" output.mp4
```

Blur video

```sh
//boxblur=9:9
ffmpeg -y -i input.mp4 -filter_complex "boxblur=2:5" output.mp4
```

Rotate video

```sh
ffmpeg -y -i inputmp4 -filter_complex "hflip,vflip" -metadata:s:v rotate=0 -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -preset superfast output.mp4

//transpose
ffmpeg -i input.mp4 -vf "transpose=2,transpose=2,format=yuv420p" -metadata:s:v rotate=0 -codec:v libx264 -codec:a copy output.mp4

//This filter can rotate to any arbitrary angle and uses radians as a unit instead of degrees. This example will rotate π/1 radians, or 180°:
ffmpeg -i input.mp4 -vf "rotate=PI:bilinear=0,format=yuv420p" -metadata:s:v rotate=0 -codec:v libx264 -codec:a copy output.mp4

//You can use degrees instead. One degree is equal to π/180 radians. So if you want to rotate 45°:
ffmpeg -i input.mp4 -vf "rotate=45*(PI/180),format=yuv420p" -metadata:s:v rotate=0 -codec:v libx264 -codec:a copy output.mp4
```

Convert to MP4

```sh
//Encode MP4 with Youtube requirement
ffmpeg -y -i input.mp4 -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -preset superfast output.mp4

//Ref
//https://trac.ffmpeg.org/wiki/Encode/YouTube
//https://trac.ffmpeg.org/wiki/Encode/H.264
```

Convert to AVI

```sh
ffmpeg -y -i input.mp4 -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -f avi -preset superfast output.avi
```

Convert to FLV

```sh
ffmpeg -y -i input.mp4 -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -f flv -preset superfast output.flv
```

Convert to MP3

```sh
ffmpeg -y -i input.mp4 -vn -acodec libmp3lame -b:a 128k -ar 44100 -bufsize 50000k -f mp3 -preset superfast output.mp3
```

Convert to GIF

```sh
//Convert .mp4 to animated gif(uncompressed) with length 30s
ffmpeg -y -i input.mp4 -s 320x240 -to 00:00:30 -preset superfast output.gif
```

Remove Audio of Video

```sh
ffmpeg -y -i input.mp4 -codec copy -an -preset superfast output.mp4
```

Add Audio to Video

```sh
ffmpeg -y -i audio.wav -i input.mp4 -codec copy -shortest -preset superfast output.mp4
```

Merge two Audio

```sh
ffmpeg -y -i audio.mp3 -i input.mp4 -filter_complex "[0:a][1:a]amix=inputs=2:duration=shortest" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -preset superfast output.mp4
```

Join many Video

```sh
//Add intro - main - outro
ffmpeg -y -i intro.mp4 -i input.mp4 -i outro.mp4 -filter_complex "[1:v]scale=1280:720,setdar=16/9 [vmain]; [1:a]volume=1.6 [amain]; [0:v]scale=1280:720,setdar=16/9 [vintro]; [2:v]scale=1280:720 [voutro]; [vintro][0:a][vmain][amain][voutro][2:a]concat=n=3:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -bufsize 500000k -preset superfast output.mp4

//Add intro - main
ffmpeg -y -i intro.mp4 -i input.mp4 -filter_complex "[1:v]scale=1280:720,setdar=16/9 [vmain]; [1:a]volume=1.6 [amain]; [0:v]scale=1280:720,setdar=16/9 [vintro]; [vintro][0:a][vmain][amain]concat=n=2:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -preset superfast output.mp4

//Add main - outro
ffmpeg -y -i outro.mp4 -i input.mp4 -filter_complex "[1:v]scale=1280:720,setdar=16/9 [vmain]; [1:a]volume=1.6 [amain]; [0:v]scale=1280:720,setdar=16/9 [voutro]; [vmain][amain][voutro][0:a]concat=n=2:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -preset superfast output.mp4
```

Audio Effect 1 - Bypass Copyright of Youtube

```sh
ffmpeg -y -i input.mp4 -af "pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1),volume=1.6" -filter_complex "scale=1280:720,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -threads 0 -preset superfast output.mp4

```

Audio Effect 2 - Bypass Copyright of Youtube
```sh
ffmpeg -y -i input.mp4 -af "pan=stereo|c0<0*c0+c1|c1<0*c0+c1,aeval=-val(0)|val(1),volume=1.6" -filter_complex "scale=1280:720,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -threads 0 -preset superfast output.mp4
```

Full Screen, Video Full Effect - Bypass Copyright of Youtube

```sh
//Change MD5 Hash, clear ID3 Tag Metadata, Encode with MP4
//atempo=1.15 «« Increase/decrease the audio speed, currently increase by 115%
//volume=1.6 «« Increase/decrease the audio volume
//pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) «« Change audio effect to bypass Youtube copyright
//setpts=PTS/1.15 «« Increase/decrease the video speed, currently increase by 115%
//crop=iw/1.2:ih/1.2 «« Increase/decrease the video zoom, currently zoom with 120%
//crop=width:height:x:y «« Crop video by width,height and location x,y
//boxblur=1:2 «« Increase/decrease the blur, max value 9:9
//scale=1280:720 «« Resize video to HD 1280x720
//hflip «« Flip the input video horizontally. ex: hflip,scale=1280:720
//vflip «« Flip the input video vertically. ex: vflip,scale=1280:720
//-b:v 1400k «« Increase/decrease the video quality

ffmpeg -y -i input.mp4 -i filter.png -af "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1)" -filter_complex "[0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=1280:720 [v1]; [v1][1:v]overlay=0:0,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast output.mp4
```

Small Screen, Video Full Effect, Overlay on background video - Bypass Copyright of Youtube

```sh
//Change MD5 Hash, clear ID3 Tag Metadata, Encode with MP4
//atempo=1.15 «« Increase/decrease the audio speed, currently increase by 115%
//volume=1.6 «« Increase/decrease the audio volume
//pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) «« Change audio effect to bypass Youtube copyright
//setpts=PTS/1.15 «« Increase/decrease the video speed, currently increase by 115%
//crop=iw/1.2:ih/1.2 «« Increase/decrease the video zoom, currently zoom with 120%
//crop=width:height:x:y «« Crop video by width,height and location x,y
//boxblur=1:2 «« Increase/decrease the blur, max value 9:9
//scale=640:360 «« Resize video to SD 640x360
//hflip «« Flip the input video horizontally. ex: hflip,scale=640:360
//vflip «« Flip the input video vertically. ex: vflip,scale=640:360
//-b:v 1400k «« Increase/decrease the video quality
//background.mp4 «« background video
//overlay=11:11 «« change the location x:y of input.mp4 video, it will overlay the
background.mp4

//Do not use filter_HD.png
ffmpeg -y -i input.mp4 -i background.mp4 -filter_complex "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1); [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=640:360 [v1]; [1:v][v1]overlay=shortest=1:x=11:y=11,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast output.mp4

//Use filter_HD.png
ffmpeg -y -i input.mp4 -i background.mp4 -i filter_HD.png -filter_complex "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1); [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=640:360 [v1]; [2:v]scale=640:360 [v2]; [v1][v2]overlay=0:0 [v3]; [1:v][v3]overlay=shortest=1:x=11:y=11,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast output.mp4
```

3D Side by Side, Video Full Effect, Not Filter 3D - Bypass Copyright of Youtube

```sh
//Please consider to change below parameter in oder to bypass copyright
//boxblur=1:2 «« ncrease/decrease the blur, max value 9:9
//colorbalance=rs=0:gs=0.6:bs=0 «« Set color balance
//colorchannelmixer=aa=0.8 «« Mix the color

//Do not use filter_3D.png
ffmpeg -y -i input.mp4 -i background.mp4 -shortest -af "atempo=1.2,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1)" -filter_complex "[0:v]setpts=PTS/1.2,boxblur=1:1,scale=640x720,colorbalance=rs=0:gs=0.6:bs=0,colorchannelmixer=aa=0.8 [SideLeft]; [0:v] setpts=PTS/1.2,boxblur=1:1,scale=640x720,colorbalance=rs=0.6:gs=0:bs=0,colorchannelmixer=aa=0.8 [SideRight]; [1:v][SideLeft] overlay=0:0 [tmp1]; [tmp1][SideRight]overlay=640:0,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast output.mp4
```

3D Side by Side, Video Full Effect, Have Filter 3D - Bypass Copyright of Youtube

```sh
//Please consider to change below parameter in oder to bypass copyright
//boxblur=1:2 «« ncrease/decrease the blur, max value 9:9
//colorbalance=rs=0:gs=0.6:bs=0 «« Set color balance
//colorchannelmixer=aa=0.8 «« Mix the color
//filter_3D.png «« the filter effect background

//Use filter_3D.png
ffmpeg -y -i input.mp4 -i background.mp4 -i "filter_3D.png" -shortest -af "atempo=1.2,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1)" -filter_complex "[0:v]setpts=PTS/1.2,boxblur=1:1,scale=640x720,colorbalance=rs=0:gs=0.6:bs=0,colorchannelmixer=aa=0.8 [SideLeft]; [0:v] setpts=PTS/1.2,boxblur=1:1,scale=640x720,colorbalance=rs=0.6:gs=0:bs=0,colorchannelmixer=aa=0.8 [SideRight]; [1:v][SideLeft] overlay=0:0 [tmp1]; [tmp1][SideRight]overlay=640:0 [tmp2]; [tmp2][2:v]overlay=0:0,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast output.mp4
```

Full Screen, Add Intro - Bypass Copyright of Youtube

```sh
ffmpeg -y -i input.mp4 -i "filter_HD.png" -i "intro.mp4" -filter_complex "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) [amain]; [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=1280:720,setdar=16/9 [v1]; [v1][1:v]overlay=0:0 [vmain]; [2:v]scale=1280:720,setdar=16/9 [vintro]; [vintro][2:a][vmain][amain]concat=n=2:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -bufsize 500000k -threads 0 -preset superfast output.mp4
```

Full Screen, Add Outro - Bypass Copyright of Youtube

```sh
ffmpeg -y -i input.mp4 -i "filter_HD.png" -i "intro.mp4" -i "outro.mp4" -filter_complex "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) [amain]; [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=1280:720,setdar=16/9 [v1]; [v1][1:v]overlay=0:0 [vmain]; [2:v]scale=1280:720,setdar=16/9 [vintro]; [3:v]scale=1280:720,setdar=16/9 [voutro]; [vintro][2:a][vmain][amain][voutro][3:a]concat=n=3:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -bufsize 500000k -threads 0 -preset superfast "output.mp4"

```

Full Screen, Merge Noise Audio - Bypass Copyright of Youtube

```sh
ffmpeg -y -i input.mp4 -i "filter_HD.png" -i "Noise.mp3" -filter_complex "[0:a][2:a]amix=inputs=2:duration=shortest,atempo=1.15; [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=1280:720 [v1]; [v1][1:v]overlay=0:0,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast output.mp4

```

Full Screen, Merge Noise Audio, Add Intro - Bypass Copyright of Youtube

```sh
//Add Noise to the original video.
// Add intro video
ffmpeg -y -i input.mp4 -i "filter_HD.png" -i "Noise.mp3" -i "intro.mp4" -filter_complex "[0:a][2:a]amix=inputs=2:duration=shortest,atempo=1.15 [amain]; [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=1280:720 [v1]; [v1][1:v]overlay=0:0,setdar=16/9 [vmain]; [3:v]scale=1280:720,setdar=16/9 [vintro]; [vintro][3:a][vmain][amain]concat=n=2:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast "output.mp4"
```

Full Screen, Filter Pixel Effect - Bypass Copyright of Youtube

```sh
//Change MD5 Hash, clear ID3 Tag Metadata, Encode with MP4
//atempo=1.15 «« Increase/decrease the audio speed, currently increase by 115%
//volume=1.6 «« Increase/decrease the audio volume
//pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) «« Change audio effect to by pass Youtube copyright
//setpts=PTS/1.15 «« Increase/decrease the video speed, currently increase by 115%
//crop=iw/1.2:ih/1.2 «« Increase/decrease the video zoom, currently zoom with 120%
//crop=width:height:x:y «« Crop video by width,height and location x,y
//boxblur=1:2 «« Increase/decrease the blur, max value 9:9
//scale=1280:720 «« Resize video to HD 1280x720
//hflip «« Flip the input video horizontally. ex: hflip,scale=1280:720
//vflip «« Flip the input video vertically. ex: vflip,scale=1280:720
//-b:v 1400k «« Increase/decrease the video quality

ffmpeg -y -i input.mp4 -i "filter_HD_Pixel1.png" -af "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1)" -filter_complex "[0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=1280:720 [v1]; [v1][1:v]overlay=0:0,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast "output.mp4"

ffmpeg -y -i input.mp4 -i "filter_HD_Pixel3.png" -af "[0:a]volume=1.5" -filter_complex "[0:v]crop=501:314:0:0,boxblur=1:2,scale=1280:720 [v1]; [v1][1:v]overlay=0:0,setdar=16/9" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast "output_px3.mp4"
```

Small Screen, Overlay on background video, Add Intro and Outro - Bypass Copyright of Youtube

```sh
//Change MD5 Hash, clear ID3 Tag Metadata, Encode with MP4
//atempo=1.15 «« Increase/decrease the audio speed, currently increase by 115%
//volume=1.6 «« Increase/decrease the audio volume
//pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) «« Change audio effect to by pass Youtube copyright
//setpts=PTS/1.15 «« Increase/decrease the video speed, currently increase by 115%
//crop=iw/1.2:ih/1.2 «« Increase/decrease the video zoom, currently zoom with 120%
//crop=width:height:x:y «« Crop video by width,height and location x,y
//boxblur=1:2 «« Increase/decrease the blur, max value 9:9
//scale=640:360 «« Resize video to SD 640x360
//hflip «« Flip the input video horizontally. ex: hflip,scale=640:360
//vflip «« Flip the input video vertically. ex: vflip,scale=640:360
//-b:v 1400k «« Increase/decrease the video quality
//background.mp4 «« background video
//overlay=11:11 «« change the location x:y of input.mp4 video, it will overlay the
background.mp4

//Use filter_HD.png
ffmpeg -y -i "input.mp4" -i "background.mp4" -i "intro.mp4" -i "outro.mp4" -filter_complex "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) [amain]; [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=640:360 [v1]; [1:v][v1]overlay=shortest=1:x=11:y=11,setdar=16/9 [vmain]; [2:v]scale=1280:720,setdar=16/9 [vintro]; [3:v]scale=1280:720,setdar=16/9 [voutro]; [vintro][2:a][vmain][amain][voutro][3:a]concat=n=3:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast "output.mp4"

//Use filter_HD.png
//ffmpeg -y -i "input.mp4" -i "background.mp4" -i "filter_HD.png" -i "intro.mp4" -i "outro.mp4" -filter_complex "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) [amain]; [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=640:360 [v1]; [2:v]scale=640:360 [v2]; [v1][v2]overlay=0:0 [v3]; [1:v][v3]overlay=shortest=1:x=11:y=11,setdar=16/9 [vmain]; [3:v]scale=1280:720,setdar=16/9 [vintro]; [4:v]scale=1280:720,setdar=16/9 [voutro]; [vintro][3:a][vmain][amain][voutro][4:a]concat=n=3:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast "output.mp4"

```

Small Screen, Overlay on this video, Add Intro and Outro - Bypass Copyright of Youtube

```sh
//Change MD5 Hash, clear ID3 Tag Metadata, Encode with MP4
//atempo=1.15 «« Increase/decrease the audio speed, currently increase by 115%
//volume=1.6 «« Increase/decrease the audio volume
//pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) «« Change audio effect to by pass Youtube copyright
//setpts=PTS/1.15 «« Increase/decrease the video speed, currently increase by 115%
//crop=iw/1.2:ih/1.2 «« Increase/decrease the video zoom, currently zoom with 120%
//crop=width:height:x:y «« Crop video by width,height and location x,y
//boxblur=1:2 «« Increase/decrease the blur, max value 9:9
//scale=640:360 «« Resize video to  SD 640x360
//hflip «« Flip the input video horizontally. ex: hflip,scale=640:360
//vflip «« Flip the input video vertically. ex: vflip,scale=640:360
//-b:v 1400k «« Increase/decrease the video quality
//background.mp4 «« background video
//overlay=11:11 «« change the location x:y of input.mp4 video, it will overlay the
background.mp4

//Do not use filter_HD.png
ffmpeg -y -i "input.mp4" -i "intro.mp4" -i "outro.mp4" -filter_complex "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) [amain]; [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=640:360 [v1]; [1:v]boxblur=9:9 [v2]; [v2][v1]overlay=shortest=1:x=11:y=11,setdar=16/9 [vmain]; [2:v]scale=1280:720,setdar=16/9 [vintro]; [3:v]scale=1280:720,setdar=16/9 [voutro]; [vintro][2:a][vmain][amain][voutro][3:a]concat=n=3:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast "output.mp4"

//Use filter_HD.png
//ffmpeg -y -i "{input}.*" -i "{input}.*" -i "filter_HD.png" -i "intro.mp4" -i "outro.mp4" -filter_complex "[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1) [amain]; [0:v]setpts=PTS/1.15,crop=iw/1.2:ih/1.2,boxblur=1:2,scale=640:360 [v1]; [2:v]scale=640:360 [v2]; [v1][v2]overlay=0:0 [v3]; [1:v]boxblur=9:9 [v4]; [v4][v3]overlay=shortest=1:x=11:y=11,setdar=16/9 [vmain]; [3:v]scale=1280:720,setdar=16/9 [vintro]; [4:v]scale=1280:720,setdar=16/9 [voutro]; [vintro][3:a][vmain][amain][voutro][4:a]concat=n=3:v=1:a=1" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -threads 0 -preset superfast "{output}.mp4"
```

Full Screen, Camera Moving Effect - Bypass Copyright of Youtube

```sh
//t*0.5 «« Increase by 0.5 to increase camera moving speed based on x axis
//t*0.2 «« Increase by 0.5 to increase camera moving speed based on y axis

ffmpeg -y -i "input.mp4" -filter_complex "[0:v]crop=in_w/1.5:in_h/1.5:(in_w-out_w)/1.5+((in_w-out_w)/1.5)*sin(t*0.5):(in_h-out_h)/1.5 +((in_h-out_h)/1.5)*sin(t*0.2),boxblur=1:1,scale=1280:720,setdar=16/9;   [0:a]volume=7" -vcodec libx264 -pix_fmt yuv420p -r 30 -g 60 -b:v 1400k -profile:v main -level 3.1 -acodec libmp3lame -b:a 128k -ar 44100 -metadata title="" -metadata artist="" -metadata album_artist="" -metadata album="" -metadata date="" -metadata track="" -metadata genre="" -metadata publisher="" -metadata encoded_by="" -metadata copyright="" -metadata composer="" -metadata performer="" -metadata TIT1="" -metadata TIT3="" -metadata disc="" -metadata TKEY="" -metadata TBPM="" -metadata language="eng" -metadata encoder="" -preset superfast "output.mp4"

```

