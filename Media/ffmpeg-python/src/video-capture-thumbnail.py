# https://www.bannerbear.com/blog/how-to-use-ffmpeg-in-python-with-examples/
import ffmpeg

(
	ffmpeg.input("test.mp4")
	.filter('thumbnail', n=100)
	.output("test_thumbnail_filter_2.png")
	.run()
)

# capture frame
# (
# 	ffmpeg.input("test.mp4", ss="00:00:15")
# 	.output("test_thumbnail.png", vframes=1)
# 	.run()
# )

# use filter
# (
# 	ffmpeg.input("input.mp4")
# 	.filter('thumbnail')
# 	.output("thumbnail_filter.png")
# 	.run()
# )