"""
https://github.com/kkroening/ffmpeg-python/issues/796
stream = ffmpeg.input("input.mp4")
stream = ffmpeg.output(stream, 'rtmp://192.168.1.6:1935/live/abc123', **{'c:v:0': 'libx264', 'crf': 23, 'x264-params': 'keyint=50:min-keyint=25:scenecut=-1', 'maxrate:0': '1300k' , 'bufsize:0': '2600k', 'preset': 'faster', 'tune': 'zerolatency', 'profile:v': 'Main', 'level': '3.1', 'c:a:0': 'aac', 'ar:0': '44100', 'b:a:0': '128k', 'flags': '+global_header', 'f': 'flv'})
stream.run()
"""

import ffmpeg

payload = {
    'video': 'test.mp4',
    'fps': 'original',
    'size': 'original',
    'rtmp': 'output.mp4', # change to rtmp://
    'bitrate': '2500',
    'bufsize': '5000',
    'preset': 'veryfast',
}

# Open the video file
media = ffmpeg.input(payload['video'], stream_loop=0, re=None)

# Set the video stream to decode and open the video codec
video_stream = media.video

# Create a new stream with the desired frame rate
if 'original' not in payload['fps']:
    video_stream = ffmpeg.filter(video_stream, 'fps', fps=payload['fps'])

if 'original' not in payload['size']:
    width, height = payload['size'].split('x')
    video_stream = ffmpeg.filter(video_stream, 'scale', width, height, force_original_aspect_ratio="decrease")

# Open the audio stream (if present) and the audio codec
audio_stream = media.audio

"""
dont apply more effect or ffmpeg cpu usage will very high !!!
merge video & audio 
"""
media = ffmpeg.concat(video_stream, audio_stream, v=1, a=1)

ffmpegProcess = (
    media
    .output(                  
        filename=payload['rtmp'],
        # video encode
        video_bitrate=f'{payload["bitrate"]}k',                    
        maxrate=f'{payload["bitrate"]}k',
        bufsize=f'{payload["bufsize"]}k',
        vcodec='libx264',
        # audio encode
        audio_bitrate='128k', # a:b
        ar='44100', # a:r
        acodec='aac',
        # result          
        # r=payload['fps'], # smooth playback 20fps (frame rate) 
        g=50, # smooth playback 20 gop size (group of pictures)
        # crf=20, # convert pixel  Constant Rate Factor (CRF)
        pix_fmt='yuv420p', # pixel formater
        preset=f'{payload["preset"]}',
        format='flv',
        threads='1'
    )
    .global_args(
        '-hide_banner',
        # '-progress', 'pipe:1'
    )
    .overwrite_output()
    .run_async(
        # pipe_stdin=True,
        # pipe_stdout=True,
        # pipe_stderr=True,
        # cmd=ffmpegPath
    )
)

ffmpegProcess.wait()