# Automation-Algorithm-Dataset

El presente algorito, tiene la funcion de determinar de manera automatizada, 3 metricas de evaluacion y analisis para cualquier articulo cientifico en idioma ingles, en formato PDF. Puede ser desde 1 solo articulo hasta la cantidad que usted quiera. (Teniendo en cuenta las limitaciones de las apis de las bases de datos a utilizar)

Las 3 metricas que se evaluan son:
Visivilidad.
Comprensibilidad.
Reproducibilidad.

Se implemento diferentes tecnologias como lo son; Scraping Web, Procesamiento de Lenguaje Natural. Analisis de datos, 


#***     LIBRERIAS      ***


Librerías estándar de Python.
No se requiere instalación adicional, incluidas en la instalación estándar de Python:

os
string
json
requests
re
mimetypes
urllib.request
ast
xml.etree.ElementTree


Instalación de las librerías
Para utilizar el algoritmo instale las siguientes librerías:

. PyPDF2
. pip install PyPDF2


. pandas
. pip install pandas

. openpyxl
. pip install openpyxl

. textstat
. pip install textstat

. fitz
. pip install PyMuPDF

. BeautifulSoup
. pip install beautifulsoup4


. spacy - pip install spacy
. Descargar e instalar el modelo de idioma "en_core_web_sm":
. python -m spacy download en_core_web_sm


. nltk
. pip install nltk
Recursos necesarios para nltk:
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('large_grammars')
nltk.download('cmudict')
nltk.download('wordnet')


. selenium
. pip install selenium
Instalar Chrome WebDriver y el PATH en tu sistema:
. from webdriver_manager.chrome import ChromeDriverManager
. driver_path = ChromeDriverManager().install()
