import re
import nltk
import string
import tokenization as tk
import importlib
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from unicodedata import normalize
importlib.reload(tk)


textoL="""Luis Miguel Gallego Basteri (San Juan, 19 de abril de 1970),1 2  conocido como Luis Miguel, es un cantante y productor mexicano.3 4 5  Nacido en Puerto Rico siendo hijo de madre italiana y padre español. Emigró a México desde temprana edad, país del que adquirió la nacionalidad en 1991.6 7  Reconocido por su estilo vocal, presencia escénica y versatilidad musical, es uno de los artistas más exitosos de Latinoamérica, lo que le otorgó el apodo honorífico de el Sol de México.8 

Ha vendido alrededor de 100 millones de discos en todo el mundo,9  y cantado en múltiples géneros y estilos, incluyendo canciones pop, baladas, boleros, tangos, jazz, big band y mariachi. También es reconocido como el único cantante latino de su generación que no cruzó al mercado anglosajón durante la «explosión latina» en la década de 1990 y, por el contrario, siguió siendo el artista con mayores ventas en esa década.10 11 12  

Comenzó su carrera en 1981, con once años, y a los catorce ganó su primer premio Grammy, convirtiéndose en el artista masculino más joven en la historia de la música en recibir dicho galardón. Desde entonces, ha ganado seis premios Grammy y otros seis premios Grammy Latinos. Además, ha obtenido catorce premios Billboard de la Música Latina, tres World Music Awards, doce premios Lo Nuestro, cinco premios Spotify, entre muchos otros. En 1991, su álbum Romance se convirtió en uno de los álbumes en español más vendidos de todos los tiempos, con 14 millones de copias.10 

Luis Miguel es el primer artista latino en tener dos álbumes certificados con disco de platino en los Estados Unidos. Su álbum Segundo romance, de 1994, le valió 35 discos de platino en América Latina. También es reconocido por Billboard como el artista con más éxitos en el Top 10 de su lista Hot Latin Songs. Es el artista latino con mayor recaudación de giras y conciertos, con casi 280 millones de dólares.13  También ostenta el récord de más presentaciones consecutivas en el Auditorio Nacional de México, con un total de 30 conciertos consecutivos14 15  así como el récord de más presentaciones en un mismo recinto, con un total de 258 conciertos.16 17  En 2020, la revista Billboard lo situó en el puesto número dos en su lista de los mejores artistas latinos de todos los tiempos.18  """

texto_limpio = tk.delete_invisible_charecter(textoL)
palabras = tk.replace_year(textoL)
resultados = {palabra: tk.eliminar_ultimos_dos_numeros(palabra) for palabra in palabras}
final_result = tk.final_result(texto_limpio)
texto_limpio = final_result

resultado = re.sub(r'(\d)\s+(\d)', r'\1\2',texto_limpio)

TextoFinal = resultado
stop_words = set(stopwords.words('spanish')) #El idioma en que se agregaran y se leeran las palabras
stop_words.update(['mientras','of','mas','dolaresnota']) #palabras que deseo retirar
Palabras_tokenizadas = word_tokenize(TextoFinal)
#filtered_sentence = [w for w in TextoFinal if not w.lower() in stop_words]
filtered_sentence = []
for w in Palabras_tokenizadas:
  if w not in stop_words:
    filtered_sentence.append(w)


#print(Palabras_tokenizadas)
print(filtered_sentence)
