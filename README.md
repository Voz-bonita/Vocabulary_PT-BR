# Web Scraping Vocabulary PT-BR :brazil:

## What is it?

This is a vocabulary containing a ton of words in portuguese (brazilian) made to expand Matheus73's *vocabulario* by collecting all words supplied by the sources

* [Dicio](https://www.dicio.com.br/)
* [Conjugacao](https://www.conjugacao.com.br/)

__Note1:__ 
Even though this repo contains the same scrapping sources of Matheus73's repo, this was done using lxml instead of BS4 (BeautifulSoup4) and inlcudes a much wider range of words.

__Note2:__
This is intended to be a PT-BR vocabulary, but at the sources of this scrappping there are PT-PT words. :portugal:

## Side files
| File | Content | Number of words | Source | Source code |
| --- | --- | --- | --- | --- |
| [`conjugacao-verbos.txt`](Text+Features/) | Infintive form verbs | 20526 | [Conjugacao](https://www.conjugacao.com.br/) | [`conjugacao-verbos_mais_usados.py`](Text+Features/) |
| [`conjugacao-verbos_conjugados.txt`](Text+Features/) | All conjugated forms of all verbs from `verbos.txt`| 1703200 (Unique) | [Conjugacao](https://www.conjugacao.com.br/) | [`conjugacao-verbos_conjugados.py`](Text+Features/)  |
| [`dicio.txt`](Text+Features/) | All words listed as *palavras mais buscadas* | 160923 | [Dicio](https://www.dicio.com.br/)  | [`dicio-palavras_mais_buscadas.py`](Text+Features/)  |

## Main files

| File | Content | Number of words | Source | Source code |
| --- | --- | --- | --- | --- |
| `vocabulary.txt` | Whole words collection | 1864779 (Unique) | [Dicio](https://www.dicio.com.br/) [Conjugacao](https://www.conjugacao.com.br/) | [`file_merge.py`](Text+Features/) |
| `vocabulary_cleansed.txt` | "Cleansed" words collection | 1703863 (Unique) | [Dicio](https://www.dicio.com.br/) [Conjugacao](https://www.conjugacao.com.br/) | [`Cleanse.py`](Text+Features/) |

## About `vocabulary_cleansed.txt`
As Matheus73 noticed, in those files there is some expressions wich are not words. This might be a good reason to discard some of those expressions, that is why there is a `vocabulary_cleansed.txt`.
