# cmd = f'ffmpeg -ss 00:00:01.00 -i "{file}" -vf "scale=320:320:force_original_aspect_ratio=decrease" -vframes 1 "{filepath}"'
# # cmd = f'ffmpeg -ss 1 -i "{file}" -vframes 1 -y "{filepath}"'
# process = execute_command(cmd)
# # print(process)