# https://trac.ffmpeg.org/wiki/How%20to%20speed%20up%20/%20slow%20down%20a%20video
import ffmpeg

media =(
    ffmpeg
    .input('test.mp4')
)

video = (
    media.video
    .filter('setpts', '0.5*PTS')    
)

audio = (
    media.audio
    .filter('atempo', '2.0')
)

(       
    ffmpeg
    .output(video, audio, 'test_speed.mp4')
    .overwrite_output()
    .run()
)