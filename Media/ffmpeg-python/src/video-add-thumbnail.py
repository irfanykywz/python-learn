import ffmpeg

stream = ffmpeg.input('test.mp4')
thumbnail = ffmpeg.input('test.png')

(
    ffmpeg
    .output(stream, thumbnail, 'test_thumbnail.mp4', c='copy', **{'c:v:1': 'png'}, **{'disposition:v:1': 'attached_pic'})
    .global_args('-map', '0')
    .global_args('-map', '1')
    .run()
)