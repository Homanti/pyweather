import requests

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_city():

    ip_address = get_ip()
    response = requests.post("http://ip-api.com/batch", json=[
        {"query": ip_address},
    ]).json()
    data = response[0]['city']
    return data