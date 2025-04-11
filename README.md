# Scraping de comentários com Análise exploratória 🤖

Projeto de análise de sentimentos e padrões em reclamações públicas de consumidores no site ReclameAqui. Usando técnicas de scraping, NLP e visualização de dados, extraímos insights úteis sobre a percepção dos usuários em relação a uma marca.

---

## 🧠 Objetivo

Coletar reclamações reais de uma empresa específica, analisar os textos com IA e gerar insights sobre sentimentos, frequência de palavras e agrupamentos temáticos.

---

## 🛠️ Tecnologias e Ferramentas

- Python
- Scraping: `selenium`
- NLP: `transformers`, `torch`, `nltk`, `unidecode`
- Visualização: `matplotlib`, `wordcloud`
- Modelos de IA: `nlptown/bert-base-multilingual-uncased-sentiment`
- Armazenamento: CSV
- Organização do projeto: estrutura modular com `src/`, `data/`, `notebooks/`

---

## 🚀 Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/reclame-ai.git
cd reclame-ai
```

2. Instale os pacotes
```
pipenv install

```

3. Rode o scraper (edite a empresa se quiser)
```
python src/scraper.py

```

4. Aplique limpeza e análise de sentimento
```
python src/nlp.py

```

5. Execute as análises no Jupyter Notebook
```
jupyter notebook --no-browser notebooks/analise_inicial.ipynb

```

---

🧑‍💻 Autor
Pedronauta
Desenvolvedor de automações e entusiasta em IA aplicada
