import requests
from config import URL_BASE, CHAVE_API

nome_cidade = input("Digite o nome da cidade: ")
url_completa = f"{URL_BASE}q={nome_cidade}&appid={CHAVE_API}&units=metric"
dados_recebidos = requests.get(url_completa).json()

if dados_recebidos['cod'] != '404':
    # dados da chave main
    principal = dados_recebidos['main']
    temperatura_corrente = principal['temp']
    print(f"A temperatura atual é: {temperatura_corrente}ºC")
    pressao_corrente = principal['pressure']
    print(f"A pressão atmosférica atual é: {pressao_corrente}hPa")
    humidade_corrente = principal['humidity']
    print(f"A humidade do ar atual é: {humidade_corrente}%")

    # dados da chave weather
    clima = dados_recebidos['weather']
    descricao_clima = clima[0]['description']
    print(f"O clima está: {descricao_clima}")
else:
    print("Cidade não encontrada")
