url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')# O método find retorna a posição do PRIMEIRO caracter da string informada.
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

# Para pegar o valor do parametro moedaOrigem

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]
print(valor)