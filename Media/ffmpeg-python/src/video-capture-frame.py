# https://www.bannerbear.com/blog/how-to-use-ffmpeg-in-python-with-examples/
import ffmpeg

# # Open the video file
# stream = ffmpeg.input('test.mp4')

# # Extract the first frame from the video and save it as an image
# frame = ffmpeg.output(stream, 'tes.png')
# ffmpeg.run(frame)

# use frames
(
	ffmpeg.input("test.mp4")
	.output('test_frame_%d.png', vframes=3)
	.run()
)


# use vf fps
# (
# 	ffmpeg.input("input.mp4")
# 	.output('frame%d.png', vf='fps=1')
# 	.run()
# )


# specifict start time for capture
# (
# 	ffmpeg.input("input.mp4", ss="00:00:15")
# 	.output('frame%d.png', vframes=3)
# 	.run()
# )