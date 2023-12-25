# https://www.bannerbear.com/blog/how-to-use-ffmpeg-in-python-with-examples/
import ffmpeg

start_time = '00:00:05' # Start time for trimming (HH:MM:SS)
end_time = '00:00:15' # End time for trimming (HH:MM:SS)

(
	ffmpeg.input("test.mp4", ss=start_time, to=end_time)
	.output("test_trim.mp4")
	.run()
)