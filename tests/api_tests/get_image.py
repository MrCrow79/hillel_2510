import requests

resp = requests.get(url='https://lms.ithillel.ua/assets/favicon/apple-touch-icon.png')

print(resp.status_code)
with open('example_image.png', 'wb') as f:
    f.write(resp.content)