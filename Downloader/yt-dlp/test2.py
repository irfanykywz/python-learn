# https://www.reddit.com/r/youtubedl/comments/skgjon/is_there_a_better_guide_to_using_ytdlp_with_python/

import yt_dlp.utils

def download_video( ffmpeg_file, cookies_file, url, HHMM):
    """Download youtube video. Ensure it has a unique hour and minute timestamp , and rsync to the youtube library folder."""
    ydl_opts = {
        'match_filter': yt_dlp.utils.match_filter_func("!is_live"),
        'match_filter': yt_dlp.utils.match_filter_func("!was_live"),
        "no_warnings": True,
        "overwrites": True,
        "restrictfilenames": True,
        "noprogress": True,
        "ffmpeg-location": ffmpeg_file,
        "prefer_ffmpeg": True,
        "download_archive": "youtube_download_archive.log",
        "cookiefile": cookies_file,
        "outtmpl" : '%(channel)s [youtube2-%(channel_id)s]/%(title)s [%(id)s].%(ext)s',
        "postprocessors": [ 
            { 
                "key" : "FFmpegVideoConvertor", 
                "preferedformat" : "mp4", 
            },
            {
                'key':'FFmpegMetadata',
                'add_metadata': True,
            },
            { 
                "key":"Exec",
                "exec_cmd": f"touch -m -t %(release_date,upload_date,modified_date|NA)s{HHMM} '%(filepath)s'",
            },
            { 
                "key":"Exec",
                "exec_cmd": "rsync --protect-args --remove-source-files -Rtvz '%(filepath)s' user@fileserver:/mnt/zpool-media2/youtube/",
            },
        ]
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
    except Exception as e: 
        print(str(e))
        # if isinstance(e, DownloadError):
        #     pass
        # elif hasattr(e, 'message'):
        #     if "Command returned error code 23" in e.message:
        #         pass
        #     else:
        #         raise(e)
        # else:
        #     raise(e)   

download_video(None, None, 'https://www.youtube.com/watch?v=QmjrLljcYSw', None)            