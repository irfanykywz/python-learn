import ffmpeg

audio = (
    ffmpeg
    .input('1.wav').audio
)

video = (
    ffmpeg
    .input('1.mp4').video
)

(
    ffmpeg
    .output(video, audio, '1_merge.mp4')
    .overwrite_output()
    .run()
)