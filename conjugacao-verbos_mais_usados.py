import requests
from lxml import etree
import time

file = open("verbos.txt", "a")
for page in range(1, 207):
    response = requests.get(f"https://www.conjugacao.com.br/verbos-populares/{page}/")

    parser = etree.HTMLParser()
    tree = etree.fromstring(response.text, parser)

    xpath = '//*[@id="content"]/div[1]/ul/li'

    for word in tree.xpath(xpath):
        file.write(word.xpath('a')[0].text + ";")

file.close()
