# Web Scraping Vocabulary PT-BR

## What is it?

This is a vocabulary containing a ton of words in portuguese (brazilian) made to "enhance" Matheus73's *vocabulario* by collecting all words supplied by the sources

* [Dicio](https://www.dicio.com.br/)
* [Conjugacao](https://www.conjugacao.com.br/)

#### Note: 
Even though this repo contains the same scrapping sources of Matheus73's repo, this was done using lxml instead of BS4 (BeautifulSoup4) and inlcudes a much wider range of words.

## Files
| File | Content | Number of words | Source | Source code |
| --- | --- | --- | --- | --- |
| `conjugacao-verbos.txt` | Infintive form verbs | 20526 | [Conjugacao](https://www.conjugacao.com.br/) | [`conjugacao-verbos_mais_usados.py`](Text+Features/) |
| `conjugacao-verbos_conjugados.txt` | All conjugated forms of all verbs from `verbos.txt`| 1703200 (Unique) | [Conjugacao](https://www.conjugacao.com.br/) | [`conjugacao-verbos_conjugados.py`](Text+Features/)  |
| `dicio.txt` | All words listed as *palavras mais buscadas* | 160923 | [Dicio](https://www.dicio.com.br/)  | [`dicio-palavras_mais_buscadas.py`](Text+Features/)  |
| `vocabulary.txt` | Whole words collection | 1864779 (Unique) | [Dicio](https://www.dicio.com.br/) [Conjugacao](https://www.conjugacao.com.br/) | [`file_merge.py`](Text+Features/) |

## About `vocabulary_cleansed.txt`
As Matheus73 noticed, in those files there is some expressions wich are not words. This might be a good reason to discard some of those expressions, that why theres is a file `vocabulary_cleansed.txt`.

* Source code [`Cleanse.py`](Text+Features/)
* Number of words `1703863`