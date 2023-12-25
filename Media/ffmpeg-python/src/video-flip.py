import ffmpeg

stream = ffmpeg.input('test.mp4')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'test_flip.mp4')
ffmpeg.run(stream)