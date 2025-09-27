import requests

url = "https://api.github.com/repos/psf/requests" 
response = requests.get(url).json()

print("Nome:", response["name"])
print("Descrição:", response["description"])
print("Stars:", response["stargazers_count"])