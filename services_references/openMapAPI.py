import requests

def procurar(nomeLugar):
    base_url = "https://nominatim.openstreetmap.org/search"
    
    params = {
        "q": nomeLugar,
        "format": "json"
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data:
        first_result = data[0]
        address = first_result.get("display_name")
        print("Endereço:", address)
        return address
    else:
        print("Local não encontrado.")