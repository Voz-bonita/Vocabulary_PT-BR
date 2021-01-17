import requests
from lxml import etree

words = open("dicio.txt", "a")
for page in range(1, 1611):
    print(page)
    response = requests.get(f"https://www.dicio.com.br/palavras-mais-buscadas/{page}/")

    parser = etree.HTMLParser()
    tree = etree.fromstring(response.text, parser)

    xpath = '//*[@id="content"]/div[2]/ul/li'

    for word in tree.xpath(xpath):
        words.write(word.xpath('a')[0].text + ";")

words.close()