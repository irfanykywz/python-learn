import ffmpeg


(
    ffmpeg
    .input('rtmp.mp4', stream_loop=-1)
    .output(
        'rtmp://a.rtmp.youtube.com/live2/rtmp-key', 
        shortest=None, 
        codec='copy',
        f='flv'
    )
    .global_args("-re")
    .run()
)