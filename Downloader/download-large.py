import requests

url="https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
response = requests.get(url, stream = True)

text_file = open("data.txt","wb")
for chunk in response.iter_content(chunk_size=1024):
    print(chunk)
    text_file.write(chunk)
text_file.close()