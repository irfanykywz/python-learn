from urllib.request import urlopen

url = ''
filename = ''

response = urlopen(url)
CHUNK = 16 * 1024
with open(filename, 'wb') as f:
    while True:
        chunk = response.read(CHUNK)
        if not chunk:
            break
        f.write(chunk)