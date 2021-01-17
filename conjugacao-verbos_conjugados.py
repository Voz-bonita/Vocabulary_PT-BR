import requests
from lxml import etree

with open("verbos.txt") as file:
    verbos = file.readline()

verbos = verbos.split(";")

conjugado = open("verbos_conjugados.txt", "a")

for verbo in verbos:
    response = requests.get(f"https://www.conjugacao.com.br/verbo-{verbo}/")

    parser = etree.HTMLParser()
    tree = etree.fromstring(response.text, parser)

    xpath = '//*[@class="f"]'

    for conjugacao in tree.xpath(xpath):
        conjugado.write(conjugacao.text + ";")

conjugado.close()