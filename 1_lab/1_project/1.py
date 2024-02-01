import requests
r = requests.get('https://google.com')
print(f"Програма запустилась з бібліотекою {requests.__name__} {requests.__version__} та отримала відоповідь від сайту: {r.status_code}")