import ffmpeg

(
	ffmpeg.input("test.mp4")
	.output("test_format.wmv")
	.run()
)