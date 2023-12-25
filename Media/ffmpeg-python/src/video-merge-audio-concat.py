import ffmpeg

audio = (
    ffmpeg
    .input('1.wav')
)

video = (
    ffmpeg
    .input('1.mp4').video
)

joined = ffmpeg.concat(video, audio, v=1, a=1).node
v3 = joined[0]
a3 = joined[1].filter('volume', 0.8)

(
    ffmpeg
    .output(v3, a3, '1_merge.mp4')
    .overwrite_output()
    .run()
)