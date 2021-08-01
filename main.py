# url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

url = ' '

# Sanitização de URL
url = url.replace(' ', '')

# Validação de URL
if url == '':
    raise ValueError('A URL está vazia')

#Separa base e os parâmetros
indice_interrogacao = url.find('?')# O método find retorna a posição do PRIMEIRO caracter da string informada.
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

# Para pegar o valor do parametro moedaOrigem
# parametro_busca = 'moedaOrigem'
# indice_parametro = url_parametros.find(parametro_busca)
# indice_valor = indice_parametro + len(parametro_busca) + 1
# valor = url_parametros[indice_valor:]
# print(valor)

# Para pegar valor quando a URL tem múltiplos parâmetros
# parametro_busca = 'moedaDestino'
# indice_parametro = url_parametros.find(parametro_busca)
# indice_valor = indice_parametro + len(parametro_busca) + 1
# indice_e_comercial = url_parametros.find('&')
# valor = url_parametros[indice_valor:indice_e_comercial]
# print(valor)

#Para funcionar para qualquer quantidade de parâmetros
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)