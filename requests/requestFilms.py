import requests


def receiveUrl(url):

    requisition = requests.get(url)

    if requisition.status_code != 200:
        return print("Deu ruim a requisição!")
    
    else:
        print(requisition.json())

receiveUrl("http://www.omdbapi.com/?apikey=apiKey=spiderman")