from extrator_url import ExtratorURL

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real'
valor_dolar = 5.50
url_extraida = ExtratorURL(url)
print(url_extraida)

moeda_origem = url_extraida.get_valor_parametro('moedaOrigem')
moeda_destino = url_extraida.get_valor_parametro('moedaDestino')
quantidade = int(url_extraida.get_valor_parametro('quantidade'))
if moeda_origem == 'dolar':
    conversao = quantidade * valor_dolar
else:
    conversao = quantidade / valor_dolar
print(conversao)