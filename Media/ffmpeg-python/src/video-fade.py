import ffmpeg
infile = "test.mp4"
outfile = str(infile) +'.crossfade.mp4'

if __name__ == '__main__':
    faded = ffmpeg.input(infile, ss=10, to=21)
    into = ffmpeg.input(infile, ss=30, to=41)
    faded = ffmpeg.filter((faded, into), 'xfade', transition="fadeblack", duration=1, offset=10)
    into = ffmpeg.input(infile, ss=60, to=71)
    faded = ffmpeg.filter((faded, into), 'xfade', transition="fadeblack", duration=1, offset=20)
    # overwrite: n="-n" means never , same for y="-y" always
    written = ffmpeg.output(faded, outfile, y="-y")
    ffmpeg.run(written)