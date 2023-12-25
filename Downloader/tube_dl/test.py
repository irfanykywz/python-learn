from tube_dl import Youtube
yt = Youtube("https://www.youtube.com/shorts/a7OumGaSOQU")
yt.formats.first().download()