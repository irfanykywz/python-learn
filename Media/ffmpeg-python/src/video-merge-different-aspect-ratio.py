import ffmpeg

"""
when video aspect ratio is different we must same it to main video
or will be error
we use scale and pad to solve it
reference : https://stackoverflow.com/questions/37327163/ffmpeg-input-link-in1v0-parameters-size-640x640-sar-169-do-not-match-the
"""

# Create an input stream for each video file
stream1 = ffmpeg.input('2.mp4')
stream1_video = (
    stream1.video
    .filter("scale", "720", "1280", force_original_aspect_ratio="decrease")
    .filter("pad", "720", "1280", -1, -1, color="black")
)
stream2 = ffmpeg.input('3.mp4')
stream2_video = (
    stream2.video
    .filter("scale", "720", "1280", force_original_aspect_ratio="decrease")
    .filter("pad", "720", "1280", -1, -1, color="black")
)

# Create a filter graph for concatenating the streams
joined = ffmpeg.concat(stream1_video, stream1.audio, stream2_video, stream2.audio, v=1, a=1).node
v3 = joined[0]
a3 = joined[1].filter('volume', 0.8)

video = ffmpeg.output(v3, a3, 'test_join.mp4')

# Start the conversion process
ffmpeg.run(video)