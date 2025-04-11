import pandas as pd
import re
import nltk
from unidecode import unidecode
from transformers import pipeline

# SETTING NLTK (Natural Language Toolkit) AND DONWLOADING STOPWORDS (é, o, de, a)
nltk.download('stopwords')
stopwords = set(nltk.corpus.stopwords.words('portuguese'))


# CLEAN TEXT FUNCTION
def clean_text(text: str):
    text = unidecode(text.lower())
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stopwords]
    return ' '.join(words)


# MODEL PRE LOAD
model = pipeline('sentiment-analysis',
                 model='nlptown/bert-base-multilingual-uncased-sentiment')


# HANDLE USING BERT MODEL
def feeling_handle(text: str):
    try:
        result = model(text[:512])
        stars = int(result[0]['label'].split(' ')[0])

        if stars <= 2:
            return 'NEGATIVO'
        elif stars == 3:
            return 'NEUTRO'
        else:
            return 'POSITIVO'

    except:
        return 'Error'


df_comments = pd.read_csv(
    r'E:\Projetos-Codes\AI-ReclamaEm\data\raw\reclamacoes.csv')
df_comments['texto_limpo'] = df_comments['conteudo'].apply(
    clean_text)  # apply usado para aplicar função no pandas
df_comments['sentimento'] = df_comments['texto_limpo'].apply(feeling_handle)
df_comments.to_csv('./data/processed/reclamacoes_processado.csv', index=False,)

print('Dados processados com sucesso!')
