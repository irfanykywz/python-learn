import ffmpeg

input = ffmpeg.input('test.mp4')
audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
video = input.video.hflip()
out = ffmpeg.output(audio, video, 'test_flip.mp4')

ffmpeg.run(out)