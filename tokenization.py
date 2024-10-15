import unicodedata
import re
from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
nltk.download('stopwords')

nltk.download('punkt_tab')

def palabras_numeros(texto):
    patron = r'\b\w*[a-zA-Z]+\w*\d+\w*\b|\b\w*\d+\w*[a-zA-Z]+\w*\b'
    palabras_con_numeros = re.findall(patron, texto)
    palabras_limpias = [re.sub(r'\d+', '', word) for word in palabras_con_numeros]
    diccionario = dict(zip(palabras_con_numeros, palabras_limpias))
    for viejo, nuevo in diccionario.items():
        texto = texto.replace(viejo, nuevo)
    return texto

def eliminar_tildes(texto):
    return "".join(c for c in unicodedata.normalize("NFKD", texto) if not unicodedata.combining(c))

def eliminar_stopwords(texto):
    stop_words = set(stopwords.words('spanish'))
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    stop_words.update(stopwords.words('english'),abecedario)
    patron = r'\b(?:' + '|'.join(stop_words) + r')\b'
    texto_filtrado = re.sub(patron, '', texto, flags=re.IGNORECASE)
    texto_filtrado = re.sub(r'\s+', ' ', texto_filtrado).strip()
    return texto_filtrado


def clean_text(text):
    text = re.sub(r'\.\d+', '', text)
    text = re.sub(r'', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r"\n", ' ', text)
    text = re.sub(r'(\d)\s(?=\d{3})', r'\1', text)
    text = eliminar_tildes(text)
    text = text.lower()
    text = palabras_numeros(text)
    return text
