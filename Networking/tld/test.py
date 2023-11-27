# https://stackoverflow.com/questions/1066933/how-to-extract-top-level-domain-name-tld-from-url
from tld import get_tld

res = get_tld("http://some.subdomain.google.co.uk", as_object=True)

print(res)
# 'co.uk'

print(res.subdomain)
# 'some.subdomain'

print(res.domain)
# 'google'

print(res.tld)
# 'co.uk'

print(res.fld)
# 'google.co.uk'

print(res.parsed_url)
# SplitResult(
#     scheme='http',
#     netloc='some.subdomain.google.co.uk',
#     path='',
#     query='',
#     fragment=''
# )