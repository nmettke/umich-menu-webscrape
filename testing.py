import requests

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/bot'
    payload = {'Body': 'south quad lunch'}
    response = requests.post(url, data=payload)

    print(response.text)
