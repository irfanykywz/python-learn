from spleeter import separator


# must run in main or will error endless loop
# https://github.com/deezer/spleeter/issues/104

if __name__ == '__main__':
	# sep = separator.Separator('spleeter:2stems')
	sep = separator.Separator('spleeter:2stems', multiprocess=False)
	sep.separate_to_file('test.mp3', 'out')