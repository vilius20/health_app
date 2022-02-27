import requests

url = "https://api.datame.pro/metrics/calories/?user_id=STWy8sznZw&start_date=2020-05-01&end_date=2020-05-03"
headers = {}
headers['authorizationtoken'] = '7e004b64-c64f-493a-bdb3-60a928712940'
response = requests.request("GET", url, headers=headers)

print(response.text)