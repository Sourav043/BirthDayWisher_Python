import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '9002974010',
  'message': 'Merry chirstmas bro',
  'key': 'textbelt',
})
print(resp.json())