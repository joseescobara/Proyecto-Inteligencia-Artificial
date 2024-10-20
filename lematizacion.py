import tokenization as tk
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
import tokenization as tk
import importlib
importlib.reload(tk)
nltk.download('punkt')


def lematizar_texto(texto):
    stemmer = SnowballStemmer('spanish')
    texto_stemmed = [stemmer.stem(palabra) for palabra in texto]
    return texto_stemmed

def tabla_frecuencias(texto, idioma='spanish'):
    frecuencias = Counter(texto)
    return frecuencias


def procesamiento_texto(texto):
    texto_limpio = tk.clean_text(texto)
    texto1= tk.eliminar_stopwords(texto_limpio)
    tokens = word_tokenize(texto1)
    lema = lematizar_texto(tokens)
    frecuencias = tabla_frecuencias(lema)
    print(frecuencias)
    return lema

#### GRAFICA
def graficar_frecuencias(frecuencias):
    df_frecuencias = pd.DataFrame(frecuencias.items(), columns=['Palabra', 'Frecuencia'])
    frecuencias_contadas = df_frecuencias['Frecuencia'].value_counts().reset_index()
    frecuencias_contadas.columns = ['Frecuencia', 'Cantidad']  # Renombrar columnas para claridad

    plt.figure(figsize=(20, 6))
    sns.barplot(x='Frecuencia', y='Cantidad', data=frecuencias_contadas, palette='viridis')
    plt.title('Distribución de Frecuencias de Palabras')
    plt.ylabel('Cantidad de Palabras')
    plt.xlabel('Frecuencia')
    plt.show()
