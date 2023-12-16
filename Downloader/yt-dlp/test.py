import yt_dlp

try:

    ydl_opts = {
    	'format': 'best[height<=360][ext=mp4]',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=QmjrLljcYSw'])

except Exception as e:
    print(str(e))