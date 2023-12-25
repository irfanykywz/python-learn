# # TODO fix charmap when filename is random
# # UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position
# cmd = f'ffprobe -v quiet -print_format json -show_format -show_streams "{file}"'
# process = execute_command(cmd)
# read = json.loads(process)
# print(read)

# build = {}
# for stream in read['streams']:
#     if stream['codec_type'] == 'video':
#         # video
#         video = stream
#         build['width'] = video['width']
#         build['height'] = video['width']
#         build['video_duration_ts'] = video['duration_ts']
#     if stream['codec_type'] == 'audio':
#         # audio
#         audio = stream
#         build['audio_duration_ts'] = audio['duration_ts']

# build['size'] = read['format']['size']
# build['duration'] = read['format']['duration']
# return build