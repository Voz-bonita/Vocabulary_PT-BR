# Web Scraping Vocabulary PT-BR

## What is it?

This is a vocabulary containing a ton of words in portuguese (brazilian) made to "enhance" Matheus73's collecting all words supplied by the sources

* [Dicio](https://www.dicio.com.br/)
* [Conjugacao](https://www.conjugacao.com.br/)





## Files
| File | Content | Number of words |
| --- | --- | --- |
| `conjugacao-verbos.txt` | Infintive form verbs | 20526 |
| `conjugacao-verbos_conjugados.txt` | All conjugated forms of all verbs from `verbos.txt`| 1703200 (Unique) |
| `dicio.txt` | All words listed as *palavras mais buscadas* at [Dicio](https://www.dicio.com.br/) | 160923 |
| `vocabulary.txt` | Whole words collection | 1864779 (Unique) |


### verbos.txt

Arquivo contém 5000 verbos oriundos do site [conjugacao](https://www.conjugacao.com.br/).

O script usado para a sua geração se encontra em: `Scripts/verbos.py`

### conjugacoes.txt

Arquivo contém todos os verbos existentes no arquivo `verbos.txt` junto com suas devidas
conjugações.

O script usado para a sua geração se encontra em: `Scripts/conjugacoes.py`

### dicio.txt

Arquivo contendo todas as palavras contidas no site [Dicio](https://www.dicio.com.br/).

__(PS: Foram retiradas expressões com mais de uma palavra e nomes)__

O script usado para a sua geração se encontra em: `Scripts/dicio.py`

### vocabulario.txt

Arquivo contendo a junção de três arquivos, sendo estes:

* conjugacoes.txt
* dicio.txt
* Vocabulário encontrado no [ime usp](https://www.ime.usp.br/~pf/dicios/index.html)

Com o resultado desses Web scraping foi possivel adicionar **429461 palavras ao vocabulario base.**

