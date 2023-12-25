import ffmpeg

input_stream = ffmpeg.input('test.mp4')
watermark_image = ffmpeg.input('test-watermark.png')

# Scale the watermark to be the same size as the input video
scaled_watermark = (
    watermark_image
    .filter('scale', 150, 150)
    .filter('colorkey', 'black', 0.3, 0.9)
    # .filter('format', 'rgba')
)

# Overlay the watermark on the input video
video_with_watermark = (
    input_stream
    # .filter('scale', -1, 360)
    .overlay(scaled_watermark)
)

# Write the output to a new file
output_stream = ffmpeg.output(video_with_watermark, input_stream.audio, 'test_watermark.mp4')

ffmpeg.run(output_stream)