probe = ffmpeg.probe(video_path)
  video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
  width = int(video_info['width'])
  height = int(video_info['height'])
  crop_size = min(width, height, 640)
  
  (
      ffmpeg
      .input(video_path)
      .output(output_file, vf=f'crop={crop_size}:{crop_size}', acodec='copy')
      .run(cmd=join("utils", "ffmpeg", "ffmpeg.exe"),
           overwrite_output=True,
           capture_stdout=True,
           capture_stderr=True)
  )