# https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
import re
print(re.findall(r'\d+', "hello 42 I'm a 32 string 30"))

url = 'https://apkmody.io/games/page/1/'
buildUrl = re.sub(r'\d+', '[NUMBER]', url)
print(buildUrl)