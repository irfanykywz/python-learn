import ffmpeg

source1 = ffmpeg.input('test.mp4')
source2 = ffmpeg.input('test.mp4')

# Here, we're using the 'scale2ref' filter to scale 'source2' to the same dimensions as 'source1'
scaled_source2 = ffmpeg.filter(source2, 'scale2ref', source1)

# We're now concatenating the videos vertically using the 'vstack' filter
final_output = ffmpeg.filter(scaled_source2, source1, 'vstack')

# Finally, we're writing the result to a new video file
ffmpeg.output(final_output, 'output.mp4').run()