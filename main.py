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
import tokenizacion as tk
import lematizacion as le
import importlib
importlib.reload(tk)
importlib.reload(le)
from collections import Counter

nltk.download('punkt')

my_texts = [["""Robyn Rihanna Fenty (Parroquia de Saint Michael, 20 de febrero de 1988), conocida simplemente como Rihanna, es una cantante, actriz, diseñadora y empresaria barbadense. Nacida en Saint Michael y criada en Bridgetown, Barbados, Rihanna hizo una audición para el productor de discos estadounidense Evan Rogers en 2003, quien la invitó a los Estados Unidos para grabar cintas de demostración. Después de firmar con Def Jam en 2005, pronto obtuvo reconocimiento con el lanzamiento de sus dos primeros álbumes de estudio, Music of the Sun (2005) y A Girl Like Me (2006), ambos influenciados por la música caribeña y alcanzaron su punto máximo dentro de los diez primeros puestos de la lista Billboard 200 de Estados Unidos.

El tercer álbum de Rihanna, Good Girl Gone Bad (2007), incorporó elementos de dance pop y estableció su estatus como símbolo sexual en la industria de la música. El sencillo «Umbrella», que encabezó las listas de éxitos, le valió a Rihanna su primer premio Grammy y la catapultó al estrellato mundial. Continuó mezclando géneros pop, dance y R&B en sus siguientes álbumes de estudio, Rated R (2009), Loud (2010), Talk That Talk (2011) y Unapologetic (2012), el último de los cuales se convirtió en su primer número uno en Billboard 200. Los álbumes generaron una serie de sencillos que encabezaron las listas de éxitos, incluidos «Rude Boy», «Only Girl (In the World)», «What's My Name?», «S&M», «We Found Love», «Where Have You Been» y «Diamonds». Su octavo álbum, Anti (2016), mostró un nuevo control creativo tras su salida de Def Jam. Se convirtió en su segundo álbum número uno en los Estados Unidos y contó con el sencillo «Work» que encabezó las listas de éxitos. Durante su carrera musical, Rihanna ha colaborado con muchos artistas, como Drake, Britney Spears, Eminem, Jay-Z, Kanye West, Adam Levine, Paul McCartney, Ne-Yo y Shakira.

Con ventas de más de 250 millones de discos y sencillos en todo el mundo, Rihanna es la segunda artista musical femenina con mayores ventas de todos los tiempos. Ha obtenido 14 números uno y 31 sencillos entre los diez primeros en los Estados Unidos y 30 entradas entre los diez primeros en el Reino Unido. Sus elogios incluyen nueve premios Grammy, 13 American Music Awards (incluido el Icon Award, por su trayectoria y contribución al mundo de la música), 12 Billboard Music Awards, siete MTV Video Music Awards (incluido el Michael Jackson Video Vanguard Award, un reconocimiento entregado a músicos que han tenido un profundo impacto en la denominada «cultura MTV», a través de su discografía y videografía3​) seis Guinness World Records y el premio del presidente de la NAACP. Spotify le otorgó el título de la artista femenina más escuchada de todos los tiempos.4​5​6​ La revista Billboard la nombró «artista digital» de la década de 2000, «artista Hot 100» de la década de 2010 y «artista mainstream» más importante de los últimos 20 años.7​8​9​10​ En 2023, fue incluida en el puesto número 68 de la lista «Los 200 mejores cantantes de todos los tiempos» de la revista Rolling Stone.11​ Es considerada por dos medios de comunicación estadounidense como la artista musical más influyente y exitosa del siglo XXI.12​13​ Time la nombró una de las 100 personas más influyentes del mundo en 2012 y 2018. Forbes la ubicó entre las diez celebridades mejor pagadas en 2012 y 2014.14​15​16​17​ A partir de 2022, es la música femenina más rica, con un patrimonio neto estimado de $1.4 mil millones.18​19​

Aparte de la música, Rihanna es conocida por su participación en causas humanitarias, proyectos empresariales y la industria de la moda. Es la fundadora de la organización sin fines de lucro Clara Lionel Foundation, la marca de cosméticos Fenty Beauty y la casa de moda Fenty bajo LVMH; ella es la primera mujer negra en encabezar una marca de lujo para LVMH.20​ Rihanna también se ha aventurado en la actuación, apareciendo en papeles importantes en Battleship (2012), Home (2015), Valerian and the City of a Thousand Planets (2017) y Ocean's 8 (2018). Fue nombrada embajadora de educación, turismo e inversión por el Gobierno de Barbados en 2018, y fue declarada Héroe Nacional de Barbados el primer día de la república parlamentaria del país en 2021, lo que le da derecho al estilo de «The Right Excelente» de por vida.21​ Rihanna encabezó el espectáculo de medio tiempo del Super Bowl LVII el 12 de febrero de 2023.
"""], ["""J. Robert Oppenheimera​ (Nueva York, 22 de abril de 1904-Princeton, Nueva Jersey; 18 de febrero de 1967) fue un físico teórico estadounidense y profesor de física en la Universidad de California en Berkeley. Es una de las personas a menudo nombradas como «padre de la bomba atómica» debido a su destacada participación en el Proyecto Manhattan, el proyecto que consiguió desarrollar las primeras armas nucleares de la historia, durante la Segunda Guerra Mundial. La primera bomba nuclear fue detonada el 16 de julio de 1945 en la Prueba Trinity, en Nuevo México, Estados Unidos. Oppenheimer declararía más tarde que le vinieron a la mente las palabras del Bhagavad-gītā: «Ahora me he convertido en la muerte, el destructor de mundos».4​b​ Oppenheimer siempre expresó su pesar por el fallecimiento de víctimas inocentes cuando las bombas nucleares fueron lanzadas contra los japoneses en Hiroshima y Nagasaki los días 6 y 9 de agosto de 1945.

Después de la guerra ocupó el cargo de asesor jefe en la recién creada Comisión de Energía Atómica de Estados Unidos y utilizó su posición para abogar por el control internacional del poder nuclear, evitar la proliferación de armamento nuclear y frenar la carrera armamentística entre Estados Unidos y la Unión Soviética. Después de provocar la ira de numerosos políticos por sus opiniones públicas se le acabaron retirando sus pases de seguridad, perdiendo el acceso a los documentos militares secretos de su país, y se le acabó despojando de su influencia política directa durante una muy publicitada audiencia en 1954. En esa década Estados Unidos vivía en el macartismo y todas aquellas personas sospechosas de simpatizar con el comunismo o simplemente de ser disidentes fueron perseguidas por el gobierno; Oppenheimer pudo continuar escribiendo, trabajando en física y dando conferencias. Nueve años después de la audiencia, los presidentes John F. Kennedy y Lyndon B. Johnson le concedieron y otorgaron respectivamente el Premio Enrico Fermi como un gesto de rehabilitación de su figura.

Oppenheimer consiguió logros notables en el campo de la física, como la aproximación de Born-Oppenheimer. También trabajó en la teoría de electrones y positrones, el proceso de Oppenheimer-Phillips de la fusión nuclear y en la primera predicción sobre el efecto túnel. Junto a sus alumnos hizo importantes contribuciones a la teoría moderna sobre las estrellas de neutrones y los agujeros negros, así como a la mecánica cuántica, la teoría cuántica de campos y las interacciones de los rayos cósmicos. Como profesor y promotor de la ciencia, se le recuerda como uno de los fundadores de la escuela estadounidense de física teórica que ganó prominencia mundial en la década de 1930. Después de la Segunda Guerra Mundial, también ocupó el puesto de director del Instituto de Estudios Avanzados de Princeton.
"""], ["""El Proyecto Manhattan (en inglés: Manhattan Project) fue un proyecto de investigación y desarrollo llevado a cabo durante la Segunda Guerra Mundial que produjo las primeras armas nucleares, liderado por los Estados Unidos con el apoyo del Reino Unido y de Canadá. Desde 1942 hasta 1946, el proyecto estuvo bajo la dirección del mayor general Leslie Groves, del Cuerpo de Ingenieros del Ejército de los Estados Unidos, mientras que el físico nuclear Robert Oppenheimer fue el director del Laboratorio Nacional de Los Álamos, en el que se diseñaron las propias bombas nucleares. La unidad militar participante en el proyecto recibió la designación de Distrito Manhattan (en inglés: Manhattan District), nombre que gradualmente sustituyó el nombre en clave oficial, Desarrollo de Materiales Sustitutos (en inglés: Development of Substitute Materials). En su transcurso el proyecto absorbió a su equivalente británico previo, el proyecto Tube Alloys. El Proyecto Manhattan comenzó de forma modesta, creciendo progresivamente hasta tener más de 130 000 empleados y alcanzar un coste de casi 2000 millones de dólares.nota 1​ Más del 90 % del presupuesto se destinó a la construcción de fábricas y a la producción de materiales fisibles, con menos del 10 % destinado al desarrollo y producción de armas. La investigación y producción tuvieron lugar en más de 30 lugares por todos los Estados Unidos, Reino Unido y Canadá.

Se desarrollaron dos tipos de bombas atómicas de forma simultánea durante la guerra: un arma de fisión de tipo balístico, relativamente sencilla, y un arma nuclear de implosión, de mayor complejidad. El diseño de fisión de la bomba Thin Man resultó ser poco práctico para su uso con plutonio, por lo que se desarrolló un arma más sencilla denominada Little Boy que utilizaba uranio-235, un isótopo que constituye solo el 0,7 % del uranio en estado natural. Los trabajadores del proyecto tuvieron dificultades para separar este isótopo del uranio-238 a causa de sus semejanzas químicas y de masa. Se emplearon tres métodos para el enriquecimiento de uranio: el uso de calutrones, la difusión gaseosa y la termoforesis. La mayoría de estos trabajos se llevaron a cabo en las instalaciones Clinton Engineer Works, en Oak Ridge (Tennessee).

Paralelamente a las investigaciones con el uranio, el proyecto continuó los trabajos de producción de plutonio. Tras quedar demostrada la viabilidad del primer reactor nuclear artificial del mundo en Chicago en el Laboratorio Metalúrgico, se diseñó el reactor de grafito X-10 en Oak Ridge y los reactores de producción en las instalaciones de Hanford Engineer Works, en los que el uranio era irradiado y transmutaba en plutonio, para posteriormente separar químicamente el plutonio del uranio. El arma nuclear de implosión Fat Man se desarrolló por medio de un diseño y desarrollo concertado en el laboratorio de Los Álamos.

El proyecto realizó también tareas de contrainteligencia sobre el programa alemán de armas nucleares. Por medio de la operación Alsos, varios miembros del Proyecto Manhattan sirvieron en Europa, en ocasiones tras las líneas enemigas, apoderándose de materiales nucleares y documentación y trasladando a científicos alemanes hacia países de los Aliados. Por otra parte, a pesar de la férrea seguridad del proyecto, varios «espías del átomo» soviéticos consiguieron infiltrarse en el programa.

El primer artefacto nuclear detonado fue una bomba de implosión en la prueba Trinity, realizada en el campo de tiro y bombardeo de Alamogordo el 16 de julio de 1945. Otras dos bombas de tipo Little Boy y Fat Man se utilizaron respectivamente un mes después en los bombardeos atómicos de Hiroshima y Nagasaki. En los años inmediatamente posteriores a la guerra, el Proyecto Manhattan llevó a cabo varias pruebas de armamento en el atolón Bikini como parte de la operación Crossroads, desarrolló nuevas armas, promocionó el desarrollo de la red de laboratorios nacionales, apoyó la investigación médica sobre la radiología y cimentó las bases de la armada nuclear. El proyecto mantuvo el control sobre la investigación y producción de armas nucleares estadounidenses hasta la formación de la Comisión de Energía Atómica de los Estados Unidos en enero de 1947."""
]]

texto_tokens = [le.procesamiento_texto(words) for text in my_texts for words in text]

final_text = [word for text in texto_tokens for word in text]
print(final_text)


frecuencias = le.tabla_frecuencias(final_text)
print(le.graficar_frecuencias(frecuencias))


bigrams = list(nltk.bigrams(texto_tokens))
 
# Contar la frecuencia de cada bigrama
contador = Counter(bigrams)

# Encontrar el bigrama más repetido y su frecuencia
bigrama_mas_comun, frecuencia = contador.most_common(1)[0]
print(f"El bigrama más común es '{bigrama_mas_comun}' con una frecuencia de {frecuencia}.")

#mediana segun bigrama
contador = Counter(bigrams)

# Extraer las frecuencias en una lista
frecuencias = list(contador.values())

# Calcular la mediana de las frecuencias
mediana_frecuencias = statistics.median(frecuencias)
rango = max(frecuencias) - min(frecuencias)
varianza = statistics.variance(frecuencias)
desviacion_estandar = statistics.stdev(frecuencias)
print(rango,varianza, desviacion_estandar)
print(f"Las frecuencias de los bigramas son: {frecuencias}")
print(f"La mediana de las frecuencias es: {mediana_frecuencias}")

