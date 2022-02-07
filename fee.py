import urllib3
import json
http =urllib3.PoolManager()

url = http.request('GET','https://bitcoinfees.earn.com/api/v1/fees/recommended')
json_obj = json.loads(url.data.decode('utf-8'))
print(json_obj)
