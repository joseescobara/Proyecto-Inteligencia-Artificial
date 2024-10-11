import re
import nltk
import string
from unicodedata import normalize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

textoL = """J. Robert Oppenheimera​ (Nueva York, 22 de abril de 1904-Princeton, Nueva Jersey; 18 de febrero de 1967) fue un físico teórico estadounidense y profesor de física en la Universidad de California en Berkeley. Es una de las personas a menudo nombradas como «padre de la bomba atómica» debido a su destacada participación en el Proyecto Manhattan, el proyecto que consiguió desarrollar las primeras armas nucleares de la historia, durante la Segunda Guerra Mundial. La primera bomba nuclear fue detonada el 16 de julio de 1945 en la Prueba Trinity, en Nuevo México, Estados Unidos. Oppenheimer declararía más tarde que le vinieron a la mente las palabras del Bhagavad-gītā: «Ahora me he convertido en la muerte, el destructor de mundos».4​b​ Oppenheimer siempre expresó su pesar por el fallecimiento de víctimas inocentes cuando las bombas nucleares fueron lanzadas contra los japoneses en Hiroshima y Nagasaki los días 6 y 9 de agosto de 1945.

Después de la guerra ocupó el cargo de asesor jefe en la recién creada Comisión de Energía Atómica de Estados Unidos y utilizó su posición para abogar por el control internacional del poder nuclear, evitar la proliferación de armamento nuclear y frenar la carrera armamentística entre Estados Unidos y la Unión Soviética. Después de provocar la ira de numerosos políticos por sus opiniones públicas se le acabaron retirando sus pases de seguridad, perdiendo el acceso a los documentos militares secretos de su país, y se le acabó despojando de su influencia política directa durante una muy publicitada audiencia en 1954. En esa década Estados Unidos vivía en el macartismo y todas aquellas personas sospechosas de simpatizar con el comunismo o simplemente de ser disidentes fueron perseguidas por el gobierno; Oppenheimer pudo continuar escribiendo, trabajando en física y dando conferencias. Nueve años después de la audiencia, los presidentes John F. Kennedy y Lyndon B. Johnson le concedieron y otorgaron respectivamente el Premio Enrico Fermi como un gesto de rehabilitación de su figura.

Oppenheimer consiguió logros notables en el campo de la física, como la aproximación de Born-Oppenheimer. También trabajó en la teoría de electrones y positrones, el proceso de Oppenheimer-Phillips de la fusión nuclear y en la primera predicción sobre el efecto túnel. Junto a sus alumnos hizo importantes contribuciones a la teoría moderna sobre las estrellas de neutrones y los agujeros negros, así como a la mecánica cuántica, la teoría cuántica de campos y las interacciones de los rayos cósmicos. Como profesor y promotor de la ciencia, se le recuerda como uno de los fundadores de la escuela estadounidense de física teórica que ganó prominencia mundial en la década de 1930. Después de la Segunda Guerra Mundial, también ocupó el puesto de director del Instituto de Estudios Avanzados de Princeton. """


Minusculas = textoL.lower()
caracteres_a_eliminar = string.punctuation + "¡“”'´«»"
texto_sin_puntuacion = Minusculas.translate(str.maketrans('', '', caracteres_a_eliminar))
trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)

Texto_sinTildes = normalize('NFKC', normalize('NFKD', texto_sin_puntuacion).translate(trans_tab))
texto_limpio = re.sub(r'[\u200b]', '', Texto_sinTildes)

patron = r'\b\w*[a-zA-Z]+\w*\d+\w*\b|\b\w*\d+\w*[a-zA-Z]+\w*\b'
palabras_con_numeros = re.findall(patron, texto_limpio)

diccionario = dict(zip(palabras_con_numeros, palabras_limpias))

for viejo, nuevo in diccionario.items():
    texto_limpio = texto_limpio.replace(viejo, nuevo)
tokens = word_tokenize(texto_limpio)
stop_words = set(stopwords.words('spanish'))
texto_filtrado = [w for w in tokens if w not in stop_words]

print("El texto sin stopwords es:")
print(texto_filtrado)
