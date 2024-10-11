import re
import nltk
import string
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from unicodedata import normalize

"""Doc: """
def lower_convert(text):
    text = text.lower()
    caracteres_a_eliminar = string.punctuation + "¡"+"“"+"”"+"'"+"´"+""+"«"+"»"
    texto_sin_puntuacion = text.translate(str.maketrans('', '', caracteres_a_eliminar))
    return texto_sin_puntuacion

def delete_tildes(text):
    cleaned_text = lower_convert(text) #utilizo la lower_convert function
    #RETIRO LAS TILDES
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    Texto_sinTildes = normalize('NFKC', normalize('NFKD', cleaned_text).translate(trans_tab))
    return Texto_sinTildes

def delete_invisible_charecter(text):
    text_without_tildes = delete_tildes(text)
    # Eliminar caracteres invisibles (como \u200b)
    clean_text = re.sub(r'[\u200b]', '',text_without_tildes)
    return clean_text #Este es texto limpio que utiliza más adelante

def replace_year(text): 
    text = delete_invisible_charecter(text)
    #REEMPLAZOS de los años correctamente
    palabra = re.findall(r'\b\d{5,}\b', text)
    return palabra #Esta función retorna las palabras 

def eliminar_ultimos_dos_numeros(palabra):
    palabra = replace_year(palabra)
    # Verificar si la palabra tiene más de 4 caracteres
    if len(palabra) > 4:
        # Usar una expresión regular para reemplazar los dos últimos dígitos
        # \d{2}$ busca exactamente 2 dígitos al final de la palabra
        nueva_palabra = re.sub(r'\d{2}$', '', palabra)
        return nueva_palabra
    return palabra  # Si la palabra tiene 4 caracteres o menos, la devuelve sin cambios

def final_result(texto_limpio):
    patron = r'\b\w*[a-zA-Z]+\w*\d+\w*\b|\b\w*\d+\w*[a-zA-Z]+\w*\b'
    # Buscar todas las palabras que contengan letras y números
    palabras_con_numeros = re.findall(patron, texto_limpio)
    palabras_limpias = [re.sub(r'\d+', '', word) for word in palabras_con_numeros]
    #print(palabras_limpias)
    diccionario = dict(zip(palabras_con_numeros, palabras_limpias))
    for viejo, nuevo in diccionario.items():
        texto_limpio = texto_limpio.replace(viejo, nuevo)
    return texto_limpio
