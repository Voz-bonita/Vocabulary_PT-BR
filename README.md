# Web Scraping Vocabulary PT-BR

## What is it?

This is a vocabulary containing a ton of words in portuguese (brazilian) made to "enhance" Matheus73's by collecting all words supplied by the sources

* [Dicio](https://www.dicio.com.br/)
* [Conjugacao](https://www.conjugacao.com.br/)

## Files
| File | Content | Number of words | Source | Source code |
| --- | --- | --- | --- | --- |
| `conjugacao-verbos.txt` | Infintive form verbs | 20526 | [Conjugacao](https://www.conjugacao.com.br/) | `conjugacao-verbos_mais_usados.py` |
| `conjugacao-verbos_conjugados.txt` | All conjugated forms of all verbs from `verbos.txt`| 1703200 (Unique) | [Conjugacao](https://www.conjugacao.com.br/) | `conjugacao-verbos_conjugados.py` |
| `dicio.txt` | All words listed as *palavras mais buscadas* | 160923 | [Dicio](https://www.dicio.com.br/)  | `dicio-palavras_mais_buscadas.py` |
| `vocabulary.txt` | Whole words collection | 1864779 (Unique) | [Dicio](https://www.dicio.com.br/) [Conjugacao](https://www.conjugacao.com.br/) | `file_merge.py` |
