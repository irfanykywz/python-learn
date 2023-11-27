import urllib

url = 'https://stackoverflow.com/thispath/thispath2/?thisparam=thisvalue&thisparam2=thisvalue#thisfragment'
# url = 'javascript:;'
extract = urllib.parse.urlparse(url)

print(extract)
# ParseResult(scheme='https', netloc='stackoverflow.com', path='/thispath/thispath2/', params='', query='thisparam=thisvalue&thisparam2=thisvalue', fragment='thisfragment')

print(extract.scheme)
print(extract.netloc)
print(extract.path)
print(extract.params)
print(extract.query)
print(extract.fragment)