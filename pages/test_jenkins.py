
import requests

r = requests.get('https://google.com')
a =  r.status_code
print(a)
assert a == 200
