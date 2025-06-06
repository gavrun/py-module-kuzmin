# partial function

from functools import partial

def url(protocol, domain, path):
    return f'{protocol}://{domain}/{path}'

api_url_1 = url('https', 'api.contoso.com', 'list_data')
print(api_url_1)

http = partial(url, 'http')
https = partial(url, 'https')

api_url_2 = https('api.contoso.com', 'list_data')
print(api_url_2)

