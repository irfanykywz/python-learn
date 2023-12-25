# https://www.bannerbear.com/blog/how-to-use-ffmpeg-in-python-with-examples/
import ffmpeg

(
	ffmpeg.input("test.mp4")
	.output('test.mp3')
	.run()
)

# custom audio codec
# (
# 	ffmpeg.input("input.mp4")
# 	.output('audio.mp3', acodec='libshine')
# 	.run()
# )