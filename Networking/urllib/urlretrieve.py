# https://stackoverflow.com/questions/31432597/trying-to-download-a-file-by-url-with-urllib-retrieve-module-object-has-no-at
import urllib.request

img_url = 'https://img.freepik.com/free-photo/christmas-lantern-with-fir-branch-decoration-snowy-table-defocused-background-generative-ai_1258-150778.jpg'
urllib.request.urlretrieve(img_url, "urlretrieve.jpg")