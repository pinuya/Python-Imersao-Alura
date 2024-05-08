import requests
import random

url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
response = requests.get(url)
data = response.json()
data[42]

secretValue = random.choice(data)
secretWord = secretValue['palavra']
tip = secretValue['dica']
print(f'A palavra secreta tem{len(secretWord)} -> {tip}')
