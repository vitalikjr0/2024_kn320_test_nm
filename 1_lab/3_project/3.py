import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(f"Звертаємось до URL: {r.url} та отримуємо відповідь: {r.status_code}")