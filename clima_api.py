import requests

CIDADES = {
    "Curitiba": {"latitude": -25.43, "longitude": -49.27},
    "Hanoi": {"latitude": 21.0278, "longitude": 105.8342}
}

BASE_URL = "https://api.open-meteo.com/v1/forecast"

for cidade, coords in CIDADES.items():
    params = {
        "latitude": coords["latitude"],
        "longitude": coords["longitude"],
        "current_weather": "true"
    }
    
    resp = requests.get(BASE_URL, params=params)
    clima = resp.json()
    
    print(f"\n=== CLIMA EM {cidade.upper()} ===")
    print("Temperatura:", clima["current_weather"]["temperature"], "°C")
    print("Vento:", clima["current_weather"]["windspeed"], "km/h")