
# LIBRARIES ON
import os
import string
import json
import requests
import re
import PyPDF2 
from PyPDF2 import PdfReader
import nltk
import spacy
import mimetypes
import urllib.request
import pandas as pd
import openpyxl
import textstat
import ast
import xml.etree.ElementTree as ET
from nltk.corpus import cmudict
from io import StringIO
import re
import fitz
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# nltk - spacy
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('large_grammars')
nltk.download('cmudict')
nlp = spacy.load("en_core_web_sm")
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import cmudict
nltk.download('wordnet', quiet=True)

# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
####################################################################################
# # LIBRERIAS OFF

# import io
# import fitz
# import sys
# import pyphen
# import ast
# import urllib.request
# nltk.download('cmudict')
# import sympy
# import mimetypes
# import pdfminer
# import pdfminer.layout
# import pdfminer.high_level
# from pdfminer.high_level import extract_text
# from pdfminer.high_level import extract_text_to_fp
# from sympy.parsing.sympy_parser import parse_expr

#os.environ['PATH'] += os.pathsep + 'C:/Users/Usuario/AppData/Local/Programs/MiKTeX/miktex/bin'
#options = Options()
#options.add_argument('--headless')  # or options.add_argument('--headless=new')
#driver = webdriver.Chrome(options=options)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# PDF Directory
dir_path = "D:/JOSE/Otros/Algorithm Automation/DirPDF"

# Complex word index
Palabras_Complejas = ['Aberration', 'Abstemious', 'Abyssal', 'Acquiesce', 'Adjudicate', 'Adroit', 'Aesthetic', 'Affable', 'Affluent', 'Alacrity', 'Altruistic', 'Amalgamate', 'Ambivalent', 'Ameliorate', 'Anachronistic', 'Analogous', 'Anathema', 'Anomaly', 'Antecedent', 'Antediluvian', 'Antiquated', 'Antithesis', 'Apathetic', 'Apocryphal', 'Approbation', 'Arbitrary', 'Arcane', 'Ardent', 'Articulate', 'Ascetic', 'Asperity', 'Assiduous', 'Assuage', 'Astringent', 'Auspicious', 'Avarice', 'Axiomatic', 'Banal', 'Belligerent', 'Benevolent', 'Benign', 'Bequeath', 'Bucolic', 'Cadence', 'Cajole', 'Capricious', 'Catharsis', 'Cerebral', 'Chicanery', 'Circumlocution', 'Circumscribe', 'Clandestine', 'Cognizant', 'Collusion', 'Complacency', 'Concomitant', 'Confluence', 'Congenial', 'Conscientious', 'Consensus', 'Consummate', 'Contemptuous', 'Contrite', 'Conundrum', 'Convivial', 'Corollary', 'Coterie', 'Credulous', 'Cryptic', 'Culpable', 'Cursory', 'Debacle', 'Deleterious', 'Demagogue', 'Denigrate', 'Derivative', 'Desultory', 'Diatribe', 'Diffident', 'Dilatory', 'Dilettante', 'Discernment', 'Discomfit', 'Disparate', 'Disseminate', 'Dissolution', 'Divisive', 'Docile', 'Duplicity', 'Ebullient', 'Effervescent', 'Efficacious', 'Effrontery', 'Egregious', 'Elegiac', 'Elucidate', 'Emanate', 'Emollient', 'Empirical']

# List_Dois 
DoiDocs = ["10.1109/JSAC.2020.3018806","10.1007/s11831-020-09496-0","10.1007/s11277-020-07108-5"]

# SECTIONS - TEXT
SECCIONES = ['introduction', 'state of the art', 'development', 'materials and methods', 'methodology', 'results', 'conclusion', 'discussion', 'Declaration of Competing Interest', 'Declaration of interests', 'Author contributions', 'Author Contribution Statement', 'author statement', 'Authors’ contribution', 'Author’s statements', 'Acknowledgements',]

SECCIONES_TABLAS = ['Table 01', 'Table 1', 'Table I', 'Table A','Table A1', 'Table B','Table B1', 'Table 01.', 'Table 1.', 'Table I.', 'Table A.','Table A1.', 'Table B.','Table B1.']

SECCIONES_FIGURAS = ['Fig.1', 'Fig. 1', 'Figure 1', 'Fig. A1', 'Fig. B2', 'Fig.1', 'Fig. 1.', 'Figure 1.', 'Fig. A1.', 'Fig. B2.', 'Fig1', 'Fig 1', 'Figure 1', 'Fig A1', 'Fig B2'] 

# EVALUATE ALGORITHM
#".cl",".as"
Extension_Code = [".proto",".cpp",".hpp",".java",".class",".jar",".py",".pyc",".pyd",".pyo",".pyw",".pyz",".ipynb",".js",".rb",".php",".php3",".php4",".php5",".phtml",".swift",".go",".scala",".hs",".lua",".html",".htm",".xhtml",".css",".xml",".xsd",".xslt",".xsl",".dtd",".json",".sql",".dockerfile","Makefile",".cmd",".bat",".ts",".tsx",".coffee",".dart",".ps1",".psm1",".psd1",".groovy",".vb",".swift",".asm",".lisp",".lsp",".fas",".fasl",".tcl",".ada",".adb",".ads",".cob",".cpy",".toml",".tsv",".avpr",".avdl",".avsc",".thrift",".der",".ber",".asn",".classpath",".ino"]

# EVALUATE EQUATIONS
Ecuation_Words = ["equation","theorem","derivative","integral","formula","integral"] #"solution", "function",

Ecuation_Patron = [
    r"\s*d([a-zA-Z]+)\s*/\s*d([a-zA-Z]+)\s*",
    r"\s*Δ([a-zA-Z]+)\s*/\s*Δ([a-zA-Z]+)\s*",
    r"\s*∂([a-zA-Z]+)\s*/\s*∂([a-zA-Z]+)\s*",
    r"\s*δ([a-zA-Z]+)\s*/\s*δ([a-zA-Z]+)\s*",
    r"π",
    r"π/2",
    r"([a-zA-Z]+)\s*([+-])\s*i\s*([a-zA-Z]+)",
    r"([a-zA-Z]+)_(\{[^\}]+\}|\d+)",
    r"([a-zA-Z]+)\s*\^(\{[^\}]+\}|\d+)",
    r"(-?[0-9]+)\s*\+\s*√\(\s*([0-9]+)\s*\+\s*([0-9]+)\s*\*\s*([a-zA-Z]+)\^2\s*\)\s*/\s*([0-9]+)",
    r"sin\s*\(\s*([a-zA-Z]+)\s*\)",
    r"cos\s*\(\s*([a-zA-Z]+)\s*\)",
    r"tan\s*\(\s*([a-zA-Z]+)\s*\)",
    r"csc\s*\(\s*([a-zA-Z]+)\s*\)",
    r"sec\s*\(\s*([a-zA-Z]+)\s*\)",
    r"cot\s*\(\s*([a-zA-Z]+)\s*\)",
    r"log_\s*\(\s*([a-zA-Z]+)\s*\)",
    r"lim┬\s*\(\s*([a-zA-Z]+)\s*\)",
    r"∫",
    r"∬",
    r"∭",
    r"∮",
    r"∯",
    r"∰",
    r"∑",
    r"√\s*\(\s*([^\)]+)\s*\)",
    r"\s*([^\s]+)\s*\^\s*([^\s]+)\s*"
]

# EVALUATE DATA
#".jpg",".png",".gif",".",
Extensions_Data = [".pdf", ".docx", ".xlsx",".xls",".xlsm", ".xlsb",".tar", ".dat",".accdb",".pptx",".rtf",".rar",".vsdx",".csv",".txt",".zip",".drawio",".gif"]

# SEARCH LICENSE BY TEXT
Texto_License = ['License', 'licencia']

# SEARCH LOGIN - BY TEXT
Texto_Sitio_Plataforma = ['Iniciar Sesion', 'Iniciar Sesión', 'Crear una cuenta', 'Cerrar Sesion', 'Cerrar Sesión', 'Sign Up', 'Sign In', 'Sign Out', 'SignUp', 'SignIn', 'SigOut']

# Regular expression to search URLs
url_regex = r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'

# To Detect if page references are found:
referencias = ["REFERENCES", "References", "Bibliography", "Biographies"]

# urls to exclude
Gestor_Exclu = [
    re.compile(r'http://doi.org'),
    re.compile(r'https://doi.org'),
    re.compile(r'http://orcid.org/'),
    re.compile(r'https://orcid.org/'),
    re.compile(r'http://www.ieee.org/'),
    re.compile(r'https://www.ieee.org/'),
    re.compile(r'http://www.elsevier.com/'),
    re.compile(r'https://www.elsevier.com/'),
    re.compile(r'http://www.crossref.org/'),
    re.compile(r'https://www.crossref.org/'),
    re.compile(r'http://link.springer.com/'),
    re.compile(r'https://link.springer.com/'),
    re.compile(r'http://creativecommons.org/'),
    re.compile(r'http://creativecommons.org/.'),
    re.compile(r'https://creativecommons.org/'),
    re.compile(r'https://creativecommons.org/.'),
    re.compile(r'http://crossmark.crossref.org/'),
    re.compile(r'https://crossmark.crossref.org/'),
    re.compile(r'http://www.ScienceDirect.com'),
    re.compile(r'https://www.ScienceDirect.com'),
    re.compile(r'http://www.sciencedirect.com/'),
    re.compile(r'https://www.sciencedirect.com/'),
    re.compile(r'http://www.springernature.com/gp'),
    re.compile(r'https://www.springernature.com/gp'),
    #re.compile(r'^https://doi.org/(?!(?:.*osf\.io)).*$', re.IGNORECASE)
    re.compile(r'http://creativecommons.org/licenses/by/4.0/'),
    re.compile(r'http://creativecommons.org/licenses/by/4.0/.'),
    re.compile(r'https://creativecommons.org/licenses/by/4.0/'),
    re.compile(r'https://creativecommons.org/licenses/by/4.0/.'),

    #----
    re.compile(r'http://refhub.elsevier.com/'),
    re.compile(r'https://refhub.elsevier.com/'),
    re.compile(r'mailto:'),
]

# Repository Urls Manager
Gestor_Bibliographi = [
    ############## -- PRINCIPALES -- ####################
    re.compile(r'https://github.com/'),
    re.compile(r'https://data.mendeley.com/'),
    re.compile(r'https://elsevier.digitalcommonsdata.com/'),
    #re.compile(r'https://www.kaggle.com/dataset/')
    #re.compile(r'https://osf.io/'),
    ############## ----------------- ####################
]

Url_Normal = []
Url_Repo = []
Url_Excl = []

# REGEX - DEPTH OF SECTIONS
# Elsevier
Elsevier_LVL_2 = r'\b\d\.\d\. \b'
Elsevier_LVL_3 = r'\b\d\.\d\.\d\. \b'
Elsevier_LVL_4 = r'\b\d\.\d\.\d\.\d\. \b'
# SPRINGER
Springer_LVL_2 = r'\b\d\.\d\ +\b'
Springer_LVL_3 = r'\b\d\.\d\.\d\ +\b'
Springer_LVL_4 = r'\b\d\.\d\.\d\.\d\ +\b'
# IEEE
Ieee_LVL_2 = r'\n([A-B]\.)\s'
Ieee_LVL_3 = r'\b \d\) \b'


# METRICS TO EVALUATE:
accesibilidad = 0
contenido = 0
reproducibilidad = 0

#                              APIS
#/////////////////////////////////////////////////////////////
#  CROSSREF API
crossapi = 'https://api.crossref.org/v1/works/'

#  IEEE API
#keyIeee = 'utatz4g65w7wneyvq7q3b5kv'
keyIeee = '52et3s479vwknzu2acuemvh6'
apiIeee = 'http://ieeexploreapi.ieee.org/api/v1/search/articles?apikey='
apiIeee2= '&format=json&max_records=25&start_record=1&sort_order=asc&sort_field=article_number&doi='

# SPRINGER API
KeySpringer = '&api_key=934b4cdc553b2ac891bff6aaf3f32a87'
apiSpringer = 'http://api.springernature.com/meta/v2/json?q=doi:'

# ELSEVIER API
apiElsevier = "https://api.elsevier.com/content/article/doi/"
KeyElsevier = "?apikey=ce0d474fc505bc443b41c23dcc9bfe45"
#KeyElsevier = "?apikey=fba9882a70dc96c204d665b416156e84"
#KeyElsevier = "?apikey=4208c0255a0f0b031b57da88824bf80f"



""" - - - - -  F U N C I O N E S  - - - - - """

# Calculate Depths - NO USING
"""
def extract_titles(filename):
    # PDF
    with open(filename, 'rb') as file:
        layout = pdfminer.layout.LAParams()
        document = pdfminer.high_level.extract_text(filename, laparams=layout)

    # Buscar Titulos, Subtítulos y Sub-subtitulos
    titles = []
    for line in document.split('\n'):
        # Todo mayuscula = Titulo
        if line.isupper():
            titles.append((line, 1))
            # 2 Espacios = Subtitulo
        elif line.startswith('  '):
            # 3 espacios o mas = Sub-subtitulo
            if line.startswith('    ') or line.startswith('   '):
                titles.append((line.strip(), 3))
            else:
                titles.append((line.strip(), 2))
    return titles
"""

# Maximum Depth: - NO USING
"""
def imprimir_maxima_profundidad(titulos):
    max_profundidad = 0
    for titulo in titulos:
        profundidad = titulo[1]
        if profundidad > max_profundidad:
            max_profundidad = profundidad
    #print("\t","* Profundidad De Secciones:", max_profundidad)
    return max_profundidad
"""

# FUNCTION VALIDATE URL
def verificar_url(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return True
        else:
            return False
    except Exception as e:
        return False
    
archivo_num = 0
start_pos = 0

# Function Search in DOI
def search_dois(start_pos, archivo_num):
    for i in range(start_pos, len(DoiDocs)):
        print()
        pos = i

        # VARIABLES TO CALCULATE VALUE (Automatic Restart)
        valueVisi = 0.65
        valueMeta = 0.5198
        valueEdit = 0.74
        

        ValueDoi=0; ValueAuthor=0; ValueTitle=0; ValueYear=0; ValueAbstract=0; ValueUrl=0; ValueLink=0;  ValueUri=0; ValueVersion=0; ValueKeyword=0; ValueOpenAccess=0; ValueOpenAccessTotal=0; ValueFullText=0; ValueSoftware=0; Valuerestringed=0; ValueSubscribe=0; Valuedownload=0; ValueparcialAccess=0; ValueOnlyMetadata=0; ValueDataset=0; ValueEmbargado=0; ValueIssn=0; ValueImagen=0

        DoiSW=0; autorSW=0; tituloSW=0; yearSW=0; keywordSW=0; IssnSW=0; abstractSW=0; linkSW=0; urlSW=0; uriSW=0; versionSW=0; accesoabiertoSW=0; openAccessTotalSW=0; fulltextSW=0; softwareSW=0; parcialAccessSW=0; downloadSW=0; SubscribeSW=0; restringedSW=0; onlymetadataSW=0; datasetSW=0; embargadoSW=0; imagenSW=0
        
        # Others
        afiliacionSW = 0
        grad_cumpli = 0
        referenciasSW = 0
        Publicador_Name = ''

        abstract = ''
        archivo_num = archivo_num + 1
        

        """ ESTABLISH CONNECTION WITH THE APIS (DB) """
        
        # Crossref
        Finalurlcros = crossapi + DoiDocs[i]
        response = requests.get(Finalurlcros)
        response_json = response.json() 

        #______# GET PUBLISHER #________#
        publicador = response_json['message']['publisher']

        ############################################################

        """ 1. INDICATORS TO ASSESS VISIBILITY """

        # Identify Publisher - Through Crossref:
        publicador = response_json['message']['publisher']

        # SPRINGER - PUBLISHER: 
        if publicador == "Springer Science and Business Media LLC" or publicador == "Springer":

            Publicador_Name = "SPRINGER"
            # ACCESSES: Open // Total Open // Restricted // Download // Subscription // Full Text:
            FinalurlSpringer = apiSpringer + DoiDocs[i] + KeySpringer
            response3 = requests.get(FinalurlSpringer)
            response3_json = response3.json()

            try:
                openAccess = response3_json["records"][0]['openaccess']
                if openAccess == "false": #"true"
                    #Restricted - Login Institution
                    restringedSW = 1
                    Valuerestringed = 1.3

                    #Only Metadata
                    onlymetadataSW = 1
                    ValueOnlyMetadata = 0.65


                    # CHECK OTHER ACCESSES [Selenium]
                    try:
                        Url_Access = response_json['message']['resource']['primary']['URL']

                        #Config Google
                        options = Options()
                        options.headless = False
                        #options.add_argument('--headless')

                        #Connection Url_Article
                        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                        driver.get(Url_Access)


                        # Search text DOWNLOAD / SUBSCRIPTION (MEMBER) / PARTIAL
                        descarga = "Buy article PDF"
                        suscripcion = "Access via your institution"
                        parcial = "This is a preview of subscription content"

                        if descarga in driver.page_source:
                            downloadSW = 1
                            Valuedownload = 0.74
                            
                        if suscripcion in driver.page_source:
                            SubscribeSW = 1
                            ValueSubscribe = 1.48
                        
                        if parcial in driver.page_source:
                            ValueparcialAccess = 1.48
                            parcialAccessSW = 1

                        driver.quit()
                    except:
                        continue

                else:
                    accesoabiertoSW = 1
                    onlymetadataSW = 1
                    ValueOpenAccess = 2.6

                    openAccessTotalSW = 1
                    ValueOpenAccessTotal = 2.96

                    fulltextSW = 1
                    ValueFullText = 0.65
            except:
                continue
                

            # Resumen  / Abstract: ▲OK▼
            try:
                abstract = response3_json["records"][0]["abstract"]
                if abstract != " " and abstract != []:
                    abstractSW = 1
                    ValueAbstract = valueMeta
            except:
                abstractSW = 0

            # keywords: ▲OK▼
            try:
                keyword = response3_json["facets"][1]["values"]
                if keyword != "" and keyword != []:
                    keywordSW = 1
                    ValueKeyword = valueMeta
                    
                else:
                    keyword = response3_json["records"][1]["keyword"]
                    if keyword != "" and keyword != []:
                        keywordSW = 1
                        ValueKeyword = valueMeta         
            except:
                keywordSW = 0


        # IEEE - PUBLISHER:
        if publicador == "Institute of Electrical and Electronics Engineers (IEEE)" or publicador == "IEEE" or publicador == "(IEEE)" or publicador == "ieee" or publicador == "Institute of Electrical and Electronics Engineers":

            Publicador_Name = "IEEE"
            FinalurlIeee = apiIeee + keyIeee + apiIeee2 + DoiDocs[i]
            response2 = requests.get(FinalurlIeee)
            response2_json = response2.json()

            try:
                # ACCESSES: Open // Total Open // Restricted // Download // Subscription // Full Text:
                openAccess = response2_json["articles"][0]['access_type']
                if openAccess == "LOCKED":
                    
                    #Restringido - Login Institution
                    restringedSW = 1
                    Valuerestringed = 1.3

                    #Only Metadatos
                    onlymetadataSW = 1
                    ValueOnlyMetadata = 0.65

                    #-------------------------
                    

                    # CHECK OTHER ACCESSES [Selenium]
                    try:
                        Url_Access = response_json['message']['resource']['primary']['URL']
                        #print("LINK ARTICULO: ",Url_Access)

                        #Config Google
                        options = Options()
                        options.headless = False
                        #options.add_argument('--headless')

                        #Connection Url_Article
                        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                        driver.get(Url_Access)


                        # XPATH - Sign in to Continue Reading
                        sign_in_btn = driver.find_element(By.XPATH, '//*[@id="full-text-section"]')
                        sign_in_btn.click()
                        time.sleep(5) 

                        # XPATH - Purchase
                        purchase_btn = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/div/xpl-login-modal/div[1]/nav/ul/li[2]')  
                        purchase_btn.click()
                        time.sleep(5)
                        

                        # Search text DOWNLOAD - SUBSCRIPTION (MEMBER)
                        descarga = "Non-Member"
                        suscripcion = "Member"

                        if descarga in driver.page_source:
                            downloadSW = 1
                            Valuedownload = 0.74
                            
                        if suscripcion in driver.page_source:
                            SubscribeSW = 1
                            ValueSubscribe = 1.48

                        driver.quit()
                    except:
                        continue

                else:
                    if ("CCBY" in openAccess) or ("OPEN_ACCESS" in openAccess) or ("Open" in openAccess):
                    
                        accesoabiertoSW = 1
                        onlymetadataSW = 1
                        ValueOpenAccess = 2.6

                        openAccessTotalSW = 1
                        ValueOpenAccessTotal = 2.96

                        fulltextSW = 1
                        ValueFullText = 0.65
            except:
                continue 

            # abstract  / Abstract: -- ▲OK▼
            try:
                abstract = response2_json["articles"][0]["abstract"]
                if abstract != " " or abstract != "":
                    abstractSW = 1
                    ValueAbstract = valueMeta
            except:
                abstractSW = 0


            # keyword: -- ▲OK▼
            try:
                keyword = response2_json["articles"][0]["index_terms"]["ieee_terms"]['terms']
                if keyword != " " and keyword != []:
                    keywordSW = 1
                    ValueKeyword = valueMeta
                    
            except:
                keywordSW = 0

        # ELSEVIER - PUBLISHER
        if publicador == "Elsevier BV" or publicador == "Elsevier Ltd.":

            Publicador_Name = "ELSEVIER"
            FinalElsevier = apiElsevier + DoiDocs[i] + KeyElsevier
            response4 = requests.get(FinalElsevier)
            root = ET.fromstring(response4.content)

            # Resumen  / Abstract: ▲OK▼
            try:
                abstract = root.find(".//{http://purl.org/dc/elements/1.1/}description").text
                if abstract != "" and abstract != " ":
                    abstractSW = 1
                    ValueAbstract = valueMeta
            except:
                abstractSW = 0

            # Keyword / ▲OK▼
            try:
                keyword = root.find(".//{http://purl.org/dc/terms/}subject").text
                if keyword != " " and keyword != "":
                    keywordSW = 1
                    ValueKeyword = valueMeta
            except:
                keywordSW = 0

            # Access
            try:
                openAccess = root.find(".//{http://www.elsevier.com/xml/svapi/article/dtd}openaccess").text
                if openAccess == "0":
                    #Restricted - Login Institution
                    restringedSW = 1
                    Valuerestringed = 1.3

                    #Only Metadatos
                    onlymetadataSW = 1
                    ValueOnlyMetadata = 0.65

                    #Parcial Acceso
                    #parcialAccessSW = 1
                    #ValueparcialAccess = 1.48

                    # CHECK OTHER ACCESSES [Selenium]
                    try:
                        Url_Access = response_json['message']['resource']['primary']['URL']
                        #print("LINK ARTICULO: ",Url_Access)

                        #Config Google
                        options = Options()
                        options.headless = False
                        #options.add_argument('--headless')

                        #Connection Url_Article
                        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                        driver.get(Url_Access)

                        # Search text DOWNLOAD - SUBSCRIPTION (MEMBER)
                        descarga = "Purchase PDF"
                        suscripcion = "Access through your institution"
                        parcial = "Article preview"

                        #print("PAGINA: ", driver.page_source)

                        if descarga in driver.page_source:
                            downloadSW = 1
                            Valuedownload = 0.74
                            
                        if suscripcion in driver.page_source:
                            SubscribeSW = 1
                            ValueSubscribe = 1.48
                        
                        if parcial in driver.page_source:
                            ValueparcialAccess = 1.48
                            parcialAccessSW = 1

                        #print("Pago descarga: ",downloadSW)
                        #print("Suscripcion: ",SubscribeSW)

                        driver.quit()
                    except:
                        continue

                else:
                    accesoabiertoSW = 1
                    onlymetadataSW = 1
                    ValueOpenAccess = 2.6

                    openAccessTotalSW = 1
                    ValueOpenAccessTotal = 2.96

                    fulltextSW = 1
                    ValueFullText = 0.65
            except:
                continue

        # AGILE - PUBLISHER
        if publicador == "Copernicus GmbH" or "Copernicus" in publicador :
            
            Publicador_Name = "AGILE"
            # CHECK OTHER ACCESSES [Selenium]
            try:
                Url_Access = response_json['message']['resource']['primary']['URL']
                #print("LINK ARTICULO: ",Url_Access)

                #Config Google
                options = Options()
                options.headless = False
                #options.add_argument('--headless')

                #Connection Url_Article
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                driver.get(Url_Access)

                # Find text
                acceso = "Open-access"
                keywords = "Keywords"

                if keywords in driver.page_source:
                    keywordSW = 1
                    ValueKeyword = valueMeta


                if acceso in driver.page_source:
                    accesoabiertoSW = 1
                    onlymetadataSW = 1
                    ValueOpenAccess = 2.6

                    openAccessTotalSW = 1
                    ValueOpenAccessTotal = 2.96
            except:
                continue


            #Abstract
            try :
                abstract = response_json['message']['abstract']
                if abstract != "" and abstract != []:
                    abstractSW = 1
                    ValueAbstract = valueMeta
            except:
                abstractSW = 0
               
        #__FILTRO ABSTRACT - CROSSREF__#
        if abstractSW != 1:
            try :
                abstract = response_json['message']['abstract']
                if abstract != "" and abstract != []:
                    abstractSW = 1
                    ValueAbstract = valueMeta
            except:
                abstractSW = 0


        """ 2. INDICATORS TO EVALUATE THE CONTENT METADATA """
        #-- DOI -- [Crossref] -- ▲OK▼
        try:
            doi = response_json ['message']['DOI']
            if doi != " " and doi != []:
                DoiSW = 1
                ValueDoi = valueMeta
        except:
            DoiSW = 0


        #-- AUTHOR -- [Crossref] -- ▲OK▼
        try:
            autor = response_json['message']['author']
            if autor != " " and autor != []:
                autorSW = 1
                ValueAuthor = valueMeta 
        except:
            autorSW = 0


        #-- TITLE -- [Crossref] -- ▲OK▼
        try:
            titulo = response_json['message']['title']  
            if titulo != " " and titulo != []:
                tituloSW = 1
                ValueTitle = valueMeta
                Nombre = titulo
        except:
            tituloSW = 0


        #-- YEAR -- [Crossref] -- ▲OK▼
        try:
            year = response_json['message']['created']['date-parts']
            if year != " " and year != []:
                yearSW= 1
                ValueYear = valueMeta
        except:
            yearSW = 0
        

        #-- URL -- [Crossref] -- ▲OK▼
        try:
            url = response_json['message']['URL']
            if url != " " and url != []:
                urlSW = 1
                ValueUrl = valueMeta
        except:
            urlSW = 0 


        #-- LINK -- [Crossref] -- ▲OK▼ 
        try:
            link = response_json['message']['link'][0]['URL']
            if link != " " and link != []:
                linkSW = 1
                ValueLink = valueMeta
        except:
            linkSW = 0
       

        #-- URI -- [Crossref] -- ▲OK▼
        try:
            uri = response_json['message']['link']
            if uri != " " and uri != []:
                uriSW = 1
                ValueUri = valueMeta
        except:
            uriSW = 0


        #-- VERSION -- [Crossref] -- ▲OK▼ 
        try:
            version = response_json['message']['link'][0]['content-version']
            if version != " " and version != []:
                versionSW = 1
                ValueVersion = valueMeta
        except:
            versionSW = 0


        #-- CLASSIFICATION CODES / ISSN -- [Crossref] -- ▲OK▼
        try:
            Issn = response_json['message']['ISSN']
            if Issn != " " and Issn != []:
                IssnSW = 1
                ValueIssn = valueMeta
        except:
            IssnSW = 0


        #-- SOFTWARE -- [Crossref] -- ▲OK▼
        try:
            software = response_json['message']['link'][0]['intended-application']
            if software != " " and software != []:
                softwareSW = 1
                ValueSoftware = valueVisi
        except:
            softwareSW = 0

        #-- AFILIATION -- [Crossref] -- ▲OK▼ - For the Degree of compliance
        try:
            afiliacion = response_json['message']['funder'][0]['name']
            if afiliacion != " " and afiliacion != []:
                afiliacionSW = 1
            else:
                afiliacionSW = 0
        except:
            afiliacionSW = 0


        #-- REFERENCES -- [Crossref] -- ▲OK▼ - For the Degree of compliance
        try:
            referencias = response_json['message']['reference']
            if referencias != " " and referencias != []:
                referenciasSW = 1
            else:
                referenciasSW = 0
        except:
            referenciasSW = 0


        # Calculate Percentage For Each Indicator
        PorcentajeVisibilidad = 0
        PorcentajeMetadatos = 0
        PorcentajeEditorial = 0
        
        accesibilidad = 0

        # BREAK FOR CYCLE OF DOI LIST, SAVE LAST INSTANCE (POSITION)
        Doi = DoiDocs[i]
        break 


    # -- VALUES TO RETURN --
    return Doi, accesibilidad, contenido, reproducibilidad, ValueDoi, ValueAuthor, ValueTitle, ValueYear, ValueAbstract, ValueUrl, ValueLink,  ValueUri, ValueVersion, ValueKeyword, ValueOpenAccess, ValueOpenAccessTotal, ValueFullText, ValueSoftware, Valuerestringed, ValueSubscribe, Valuedownload, ValueparcialAccess, ValueOnlyMetadata, ValueDataset, ValueEmbargado, imagenSW, ValueIssn, DoiSW, autorSW, tituloSW, yearSW, keywordSW, IssnSW, abstractSW, linkSW, urlSW, uriSW, versionSW, accesoabiertoSW, openAccessTotalSW, fulltextSW, softwareSW, parcialAccessSW, downloadSW, SubscribeSW, restringedSW, onlymetadataSW, datasetSW, embargadoSW, ValueImagen, afiliacionSW, referenciasSW, abstract, valueVisi, valueMeta, valueEdit, Nombre, archivo_num, grad_cumpli, publicador, Publicador_Name


# Loop through PDF and count // Function call.(D)
for filename in os.listdir(dir_path):    
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(dir_path, filename)

        # -- CALL FUNCTION --
        # call DOI search function
        Doi, accesibilidad, contenido, reproducibilidad, ValueDoi, ValueAuthor, ValueTitle, ValueYear, ValueAbstract, ValueUrl, ValueLink,  ValueUri, ValueVersion, ValueKeyword, ValueOpenAccess, ValueOpenAccessTotal, ValueFullText, ValueSoftware, Valuerestringed, ValueSubscribe, Valuedownload, ValueparcialAccess, ValueOnlyMetadata, ValueDataset, ValueEmbargado, imagenSW, ValueIssn, DoiSW, autorSW, tituloSW, yearSW, keywordSW, IssnSW, abstractSW, linkSW, urlSW, uriSW, versionSW, accesoabiertoSW, openAccessTotalSW, fulltextSW, softwareSW, parcialAccessSW, downloadSW, SubscribeSW, restringedSW, onlymetadataSW, datasetSW, embargadoSW, ValueImagen, afiliacionSW, referenciasSW, abstract, valueVisi, valueMeta, valueEdit, Nombre, archivo_num, grad_cumpli, publicador, Publicador_Name = search_dois(start_pos, archivo_num)



        # MULTIMEDIA - ACCESIBILIDAD - VERSION 1.0
        """
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            image_found = False

            for page in reader.pages:
                if '/XObject' in page['/Resources']:
                    x_objects = page['/Resources']['/XObject'].getObject()
                    if x_objects:
                        for obj in x_objects:
                            if x_objects[obj]['/Subtype'] == '/Image':
                                image_found = True
                                break

                if image_found:
                    imagenSW = 1
                    ValueImagen = valueMeta
                    break

        print("MULTIMEDIA METODO 1: ", imagenSW,"\n")   
        """

        # MULTIMEDIA - ACCESSIBILITY - VERSION 2.0
        pdf_file = fitz.open(pdf_path)
        for page_index in range(len(pdf_file)):
            page = pdf_file[page_index]
            image_list = page.get_images()
            if image_list:
                imagenSW = 1
                ValueImagen = valueMeta
                break
        print("MULTIMEDIA: ", imagenSW,"\n") 



        #FINAL ABSTRACT FILTER - EXTRACT FROM THE DOCUMENT
        if abstractSW == 0:
            pdf_reader = PyPDF2.PdfReader(pdf_path)

            num_pages = len(pdf_reader.pages)
            all_text = ''
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                all_text += page_text

            # Look for the pattern of the abstract
            abstract_pattern = re.compile(r'abstract', re.IGNORECASE)
            match = abstract_pattern.search(all_text)

            # Extract the text from the abstract
            if match:
                abstract_text = all_text[match.start():]
                next_heading = re.compile(r'^\s*(1\.|i\.|a\.)\s', re.MULTILINE)
                match = next_heading.search(abstract_text)
                if match:
                    abstract_text = abstract_text[:match.start()]

                # Look for the pattern of the introduction
                intro_pattern = re.compile(r'^(1|I)\.\s*INTRODUCTION', re.MULTILINE)
                match = intro_pattern.search(all_text)
                if match:
                    intro_text = all_text[match.start():]
                    abstract_text += intro_text

                # Look for the pattern of the keywords
                keywords_pattern = re.compile(r'^(1|I{1,3})?\.\s*(KEYWORDS|Keywords)', re.MULTILINE)
                match = keywords_pattern.search(all_text)
                if match:
                    keywords_text = all_text[match.start():]
                    abstract_text += keywords_text
        
            abstract = abstract_text
            abstractSW = 1
            ValueAbstract = valueMeta


        #_______________▲▼_______________# LEXICAL DENSITY #______________▲▼__________________#
        DL_palabras = abstract.split()
        DL_total_palabras = len(DL_palabras) # N
        DL_vocabulario = set(DL_palabras)  
        DL_total_vocabulario = len(DL_vocabulario)  # V
        
        Densidad_Lexica = DL_total_vocabulario / DL_total_palabras  * 3.49

        # Normalizar SIN PESO
        #Norm_Densidad_lexica = (Densidad_Lexica - 0) / (DL_total_palabras - 0)
        # Normalizar CON PESO
        #Norm_Densidad_lexica_Peso = (Densidad_Lexica - 0) / (DL_total_palabras - 0) * 3.49


        #print("*********************** COMPRESNIBILIDAD  *************************")
        #print("******* DENSIDAD LEXICA *********")
        #print("Densidad Lexica: ",Densidad_Lexica)
        #print("Densidad Lexica: ",Densidad_Lexica)
        #print("Densidad Lexica-Normalizada: ",Norm_Densidad_lexica)
        #print("Densidad Lexica-Normalizada Con Peso: ",Norm_Densidad_lexica_Peso)
        #print("********************************","\n")
        

        #_____________▲▼________________# COMPLEJIDAD DE LA ORACION #______________▲▼__________________#
        

        CO_oraciones = nltk.sent_tokenize(abstract)
        palabras_por_oracion = [len(nltk.word_tokenize(oracion)) for oracion in CO_oraciones]
        indice_longitud_oracional = sum(palabras_por_oracion) / len(palabras_por_oracion)

        nlp = spacy.load('en_core_web_sm')
        
        # function to check if a sentence is complex
        def is_complex(sentence):
            doc = nlp(sentence)
            clauses = [chunk for chunk in doc.noun_chunks if chunk.root.dep_ == 'nsubj']
            for token in doc:
                if token.dep_ == 'mark':
                    clauses.append(token.text)
            if len(clauses) > 1:
                return True
            else:
                return False

        # Split abstract into sentences
        sentences = nltk.sent_tokenize(abstract)

        # Calculate the number of complex phrases per sentence
        complex_sentence_index = []
        complex_sentences_list = []
        for sentence in sentences:
            words = len(nltk.word_tokenize(sentence))
            if words > 0:
                if is_complex(sentence):
                    complex_sentences_list.append(sentence)
                complex_sentences = sum([is_complex(subsentence) for subsentence in nltk.sent_tokenize(sentence)])
                complex_sentence_index.append(complex_sentences / words)

        # Average number of complex phrases per sentence [Index]
        average_complex_sentence_index = sum(complex_sentence_index) / len(complex_sentence_index)


        # Words
        palabras = nltk.word_tokenize(abstract)
        palabras2 = len(palabras)
        # Sentences
        oraciones = nltk.sent_tokenize(abstract)
        oracion2 = len(oraciones)

        # complex words:
        frases_complejas = len(complex_sentences_list)
        
        #Calculation
        Complejidad_Oracion = (0.4 * (palabras2/oracion2) + 100 * (frases_complejas/palabras2))

        
        Nor_Complejidad_Oracion = (Complejidad_Oracion - 6) / (17 - 6)
        Nor_Complejidad_Oracion_Peso =  (Complejidad_Oracion - 6) / (17 - 6) * 3.49

        
        #print("******* COMPLEJIDAD DE LA ORACION *********")
        #print("Complejidad Oracion: ",Complejidad_Oracion)
        #print("Complejidad Oracion-Normalizada: ", Nor_Complejidad_Oracion)
        #print("Complejidad Oracion-Normalizada Con Peso: ", Nor_Complejidad_Oracion_Peso)
        #print("********************************","\n")
        

        #________________▲▼___________# COMPLEJIDAD SINTACTICA #_____________▲▼________________#


        # Num words
        palabras = nltk.word_tokenize(abstract)
        nume_palabras = len(palabras)

        # number of sentences - Sentence Length
        oraciones = nltk.sent_tokenize(abstract)
        num_oraciones = len(oraciones)

        # Num Modifiers
        num_modifiers = 0
        for palabra in palabras:
            tag = nltk.pos_tag([palabra])[0][1]
            if tag.startswith('JJ') or tag.startswith('RB'):
                num_modifiers += 1
        
        # Average Modifiers Per Sentence.
        promedio_modificadores_oracion = (num_modifiers / num_oraciones)

        # Formula Syntactic Complexity: ((total number of sentences x average number of modifiers per sentence) / total number of words)
        Complejidad_Sintactica = (num_oraciones * promedio_modificadores_oracion) / nume_palabras
        # Normalize would look like this (value - 0) / (LO - 0)
        Norm_Complejidad_Sintactica = (Complejidad_Sintactica - 0) / (num_oraciones - 0)
        # Normalize With Weight - Sentence Length
        Norm_Complejidad_Sintactica_Peso = (Complejidad_Sintactica - 0) / (num_oraciones - 0) * 3.49

        
        #print("******* COMPLEJIDAD SINTACTICA *********")
        #print("Complejidad Sintactica: ",Complejidad_Sintactica)
        #print("Complejidad Sintactica-Normalizar: ",Norm_Complejidad_Sintactica)
        #print("Complejidad Sintactica-Normalizar Con Peso: ",Norm_Complejidad_Sintactica_Peso)
        #print("********************************","\n")
        

        #_______________▲▼_______________# SCORE MARKS #______________▲▼__________________#


        patron = r'[^\w\s]'
        num_puntuacion = len(re.findall(patron, abstract))
        Marcas_Puntuacion = num_puntuacion / len(abstract)

        # Normalize (average–0) / (ns– 0) ns= number of signs
        Norm_Marcas_Puntuacion = (Marcas_Puntuacion - 0) / (num_puntuacion - 0)
        # Normalize With Weight
        Norm_Marcas_Puntuacion_Peso = (Marcas_Puntuacion - 0) / (num_puntuacion - 0) * 3.49
        
        
        #print("******* MARCAS DE PUNTUACION *********")
        #print("Marcas puntuacion: ",Marcas_Puntuacion)
        #print("Marcas puntuacion-Normalizar: ",Norm_Marcas_Puntuacion)
        #print("Marcas puntuacion-Normalizar Con Peso: ",Norm_Marcas_Puntuacion_Peso)
        #print("********************************","\n")




        # call Depth Function.
        d = cmudict.dict()

        # -- CALCULATE VALUES (NUM: Words, Sentences, Letters, Syllables)
         # tokenize
        palabras = word_tokenize(abstract)
        oraciones = sent_tokenize(abstract)
        # Number of words and sentences
        num_palabras = len(palabras)
        num_oraciones = len(oraciones)
        # Number of letters and syllables
        num_letras = sum(len(palabra) for palabra in palabras)
        num_silabas = sum(len(d.get(palabra.lower(), [0])) for palabra in palabras)

        num_palabras_complejas = len([palabra for palabra in palabras if palabra in Palabras_Complejas])

        # Advance to the next DOI in the DoiDocs list.
        start_pos = start_pos + 1

        #_________________▲▼_______________# INDEX SSR #______________▲▼_________________#

        def calculate_ssr(abstract):
            s = abstract.count('.') + abstract.count('!') + abstract.count('?')
            w = len(abstract.split())
            
            # List of rare (complex) words for English
            Palabras_Complejas = ['Aberration', 'Abstemious', 'Abyssal', 'Acquiesce', 'Adjudicate', 'Adroit', 'Aesthetic', 'Affable', 'Affluent', 'Alacrity', 'Altruistic', 'Amalgamate', 'Ambivalent', 'Ameliorate', 'Anachronistic', 'Analogous', 'Anathema', 'Anomaly', 'Antecedent', 'Antediluvian', 'Antiquated', 'Antithesis', 'Apathetic', 'Apocryphal', 'Approbation', 'Arbitrary', 'Arcane', 'Ardent', 'Articulate', 'Ascetic', 'Asperity', 'Assiduous', 'Assuage', 'Astringent', 'Auspicious', 'Avarice', 'Axiomatic', 'Banal', 'Belligerent', 'Benevolent', 'Benign', 'Bequeath', 'Bucolic', 'Cadence', 'Cajole', 'Capricious', 'Catharsis', 'Cerebral', 'Chicanery', 'Circumlocution', 'Circumscribe', 'Clandestine', 'Cognizant', 'Collusion', 'Complacency', 'Concomitant', 'Confluence', 'Congenial', 'Conscientious', 'Consensus', 'Consummate', 'Contemptuous', 'Contrite', 'Conundrum', 'Convivial', 'Corollary', 'Coterie', 'Credulous', 'Cryptic', 'Culpable', 'Cursory', 'Debacle', 'Deleterious', 'Demagogue', 'Denigrate', 'Derivative', 'Desultory', 'Diatribe', 'Diffident', 'Dilatory', 'Dilettante', 'Discernment', 'Discomfit', 'Disparate', 'Disseminate', 'Dissolution', 'Divisive', 'Docile', 'Duplicity', 'Ebullient', 'Effervescent', 'Efficacious', 'Effrontery', 'Egregious', 'Elegiac', 'Elucidate', 'Emanate', 'Emollient', 'Empirical']
            
            # Number of rare words in the text
            rw = len([word for word in abstract.split() if word.lower() in Palabras_Complejas])
            
            # Calculation of the SSR index
            ssr = (1.609 * (w/s)) + (331.8 * (rw/w)) + 22.0
            
            return ssr

        text = abstract
        ssr = calculate_ssr(text)

        # RANKS TO BE: 
        # # Very simplified
        if ssr <= 39:
            rangoSSR = "Muy Simplificado"
        # Very easy
        if ssr >= 40 and ssr <= 60:
            rangoSSR = "Muy Facil"
        # Easy
        if ssr >= 61 and ssr <= 80:
            rangoSSR = "Facil" 
        # Moderate difficulty
        if ssr >= 81 and ssr <= 100:
            rangoSSR = "Dificultad Moderada"
        # Difficult
        if ssr >= 101 and ssr <= 120:
            rangoSSR = "Dificil"
        # Very difficult
        if ssr >= 121:
            rangoSSR = "Muy Dificil"

        # normalize
        Norm_ssr = (ssr - 0) / (121 - 0)
        # Normalize With Weight
        Norm_ssr_Peso = (ssr - 0) / (121 - 0) * 1.27

        
        #print("******* INDICE SSR *********")
        #print("SRR: ", ssr,"\t", "Rango: ",rangoSSR)
        #print("SSR-Normalizado: ",Norm_ssr)
        #print("SSR-Normalizado Con Peso: ",Norm_ssr_Peso)
        #print("********************************","\n")
        

        #_________________________________# FACILIDAD DE LECTURA #___________________________________#

        palabras = word_tokenize(abstract)
        oraciones = sent_tokenize(abstract)
        num_palabras = len(palabras)
        num_oraciones = len(oraciones)

        d = cmudict.dict()
        num_silabas = sum(len(d.get(palabra.lower(), [0])) for palabra in palabras)

        Facilidad_Lectura = 206.835 - 1.015 * (num_palabras/num_oraciones) - 84.6 * (num_silabas/num_palabras)
        # Normalizar  (valor – 0) / (100– 0) 
        Norm_Facilidad_Lectura = (Facilidad_Lectura - 0) / (100 - 0) 
        # Normalizar Con Peso
        Norm_Facilidad_Lectura_Peso = (Facilidad_Lectura - 0) / (100 - 0) * 1.27

        
        #print("******* FACILIDAD DE LECTURA *********")
        #print("Facilidad Lectura:", Facilidad_Lectura)
        #print("Facilidad Lectura-Norm:", Norm_Facilidad_Lectura)
        #print("Facilidad Lectura-Norm Con Peso:", Norm_Facilidad_Lectura_Peso)
        #print("********************************","\n")
         

        #_________________________________# TEXT ANALYSIS - TREE #___________________________________#

        doc = nlp(abstract)
        Densidad_Arbol = len(doc) / (len(doc) + 1)
        #print("DENSIDAD ARBOL NO PESO: ", Densidad_Arbol)
        Densidad_Arbol = Densidad_Arbol * 1.27
        #print("DENSIDAD ARBOL PESO: ", Densidad_Arbol, "\n")


        # Normalizar (valor - 0) / (1 - 0)
        # Norm_Arbol = (depth - 1) / (Mayor_Profundidad - 1)
        # Normalizar Con Peso
        #Norm_Arbol_Peso = (depth - 1) / (Mayor_Profundidad - 1) * 7.08


        
        #print("******* PROFUNDIDAD ARBOL *********")
        #print("Profundidad Arbol :", Densidad_Arbol)
        #print("Profundidad Arbol-Norm",Norm_Arbol)
        #print("Profundidad Arbol-Norm Con Peso",Norm_Arbol_Peso)
        #print("********************************","\n")
        

        #_________________________________# DEGREE OF COMPLIANCE #___________________________________#

        """
        titulo. -- META -- ▲OK▼ 
        autores. -- META -- ▲OK▼ 
        filiacion. -- META -- ▲OK▼ 
        num palabras y tablas / figuras.    ****
        declaracion de conflicto de interes. -- TEXT -- ▲OK▼ 
        abstract. -- META -- ▲OK▼ 
        key words. -- META -- ▲OK▼ 
        introduccion. -- TEXT -- ▲OK▼ 
        metodos/Metodologia. -- TEXT -- ▲OK▼ 
        resultados. -- TEXT -- ▲OK▼ 
        discucion.  -- TEXT -- ▲OK▼ 
        conclucion. -- TEXT -- ▲OK▼ 
        agradecimineto. -- TEXT -- ▲OK▼ 
        contribucion autores.-- TEXT -- ▲OK▼ 
        referencias. -- META -- ▲OK▼ 
        tablas. -- TEXT -- ▲OK▼ 
        figuras. -- TEXT -- ▲OK▼ 
        """

        grad_cumpli_doc = 0

        if tituloSW == 1:
            grad_cumpli = grad_cumpli + 1
        if autorSW == 1:
            grad_cumpli = grad_cumpli + 1
        if afiliacionSW == 1:
            grad_cumpli = grad_cumpli + 1
        if abstractSW == 1:
            grad_cumpli = grad_cumpli + 1
        if keywordSW == 1:
            grad_cumpli = grad_cumpli + 1
        if referenciasSW == 1:
            grad_cumpli = grad_cumpli + 1

        with open(os.path.join(dir_path, filename), 'rb') as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)

            
            texto = ''
            for pagina in lector_pdf.pages:
                texto += pagina.extract_text()

            
            titulos = {}

            # Sections
            for seccion in SECCIONES:
                inicio = texto.find(seccion)
                if inicio != -1:
                    fin_linea = texto.find('\n', inicio)
                    titulo = texto[inicio:fin_linea].strip()
                    grad_cumpli_doc += 1
                    titulos[seccion] = titulo

            # boards
            for seccion in SECCIONES_TABLAS:
                inicio = texto.find(seccion)
                if inicio != -1:
                    fin_linea = texto.find('\n', inicio)
                    titulo = texto[inicio:fin_linea].strip()
                    titulos[seccion] = titulo
                    grad_cumpli_doc += 1
                    break
            
            # Figures
            for seccion in SECCIONES_FIGURAS:
                inicio = texto.find(seccion)
                if inicio != -1:
                    fin_linea = texto.find('\n', inicio)
                    titulo = texto[inicio:fin_linea].strip()
                    titulos[seccion] = titulo
                    grad_cumpli_doc += 1
                    break

            
            Grado_Cumplimiento = len(titulos)
            Grado_Cumplimiento = Grado_Cumplimiento + grad_cumpli
            # Normalizar
            Norm_Grado_Cumplimiento = (Grado_Cumplimiento - 1) / (15 - 1)
            # Normalizar Con Peso
            Norm_Grado_Cumplimiento_Peso = (Grado_Cumplimiento - 1) / (15 - 1) * 7.08

            
            #print("******* GRADO DE CUMPLIMIENTO *********")
            #print("Grado De Cumplimiento: ",Grado_Cumplimiento)
            #print("Grado Cumplimiento-Norm: ", Norm_Grado_Cumplimiento)
            #print("Grado Cumplimiento-Norm Con Peso: ", Norm_Grado_Cumplimiento_Peso)
            #print("********************************","\n")       

        #______________________________# PROFUNDIDAD DE SECCIONES #_______________________________#


        nivel_2_titulos = []
        nivel_3_titulos = []
        nivel_4_titulos = []

        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                content = page.extract_text()

                if Publicador_Name == "ELSEVIER":
                    nivel_2_titulos.extend(re.findall(Elsevier_LVL_2, content))
                    nivel_3_titulos.extend(re.findall(Elsevier_LVL_3, content))
                    nivel_4_titulos.extend(re.findall(Elsevier_LVL_4, content))

                if Publicador_Name == "SPRINGER":
                    nivel_2_titulos.extend(re.findall(Springer_LVL_2, content))
                    nivel_3_titulos.extend(re.findall(Springer_LVL_3, content))
                    nivel_4_titulos.extend(re.findall(Springer_LVL_4, content))
                
                if Publicador_Name == "IEEE":
                    nivel_2_titulos.extend(re.findall(Ieee_LVL_2, content))
                    nivel_3_titulos.extend(re.findall(Ieee_LVL_3, content))

        #print(f"Archivo: {pdf_path}")
        #print(f"Nivel 2: ",nivel_2_titulos)
        #print(f"Nivel 3: ",nivel_3_titulos)
        #print(f"Nivel 4: ",nivel_4_titulos)
        

        
        Profundidad_Secciones = 1

        if nivel_4_titulos:
            Profundidad_Secciones = 4
        elif nivel_3_titulos:
            Profundidad_Secciones = 3
        elif nivel_2_titulos:
            Profundidad_Secciones = 2

        # Normalizar (valor – 1) / (4 – 1) 
        Norm_Profundidad_Secciones = (Profundidad_Secciones - 1) / (4 - 1)
        # Normalizar Con Peso
        Norm_Profundidad_Secciones_Peso = (Profundidad_Secciones - 1) / (4 - 1) * 7.08

        # En caso de que de 0
        if Norm_Profundidad_Secciones_Peso == 0:
            Norm_Profundidad_Secciones_Peso = 1

         
        #print("******* PROFUNDIDAD DE SECCIONES *********")
        #print("Profundidad Secciones: ",Profundidad_Secciones)
        #print("Profundidad Secciones-Norm: ",Norm_Profundidad_Secciones)
        #print("Profundidad Secciones-Norm Con Peso",Norm_Profundidad_Secciones_Peso)

        
        


        #///////////////////////////# PROCENTAJES #/////////////////////////////#

        # TOTAL PERCENTAGES CONTENT
        TotalComprensibilidad = Densidad_Lexica + Nor_Complejidad_Oracion_Peso + Norm_Complejidad_Sintactica_Peso + Norm_Marcas_Puntuacion_Peso
        TotalLegibilidad = Norm_ssr_Peso + Norm_Facilidad_Lectura_Peso + Densidad_Arbol
        TotalContenidos = Norm_Grado_Cumplimiento_Peso + Norm_Profundidad_Secciones_Peso
        Contenidos = TotalComprensibilidad + TotalLegibilidad + TotalContenidos
        


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        """ 3. REPRODUCIBILIDAD"""
        #EXAMINANDO REPRODUCIBILIDAD VER. 1.0
        """
        found_references = False
        # Algoritmo
        SW_Algoritmo = 0;SW_A_Repo = 0;SW_A_Plataforma = 0;SW_A_Sitio = 0;SW_A_Tipo_recurso = 0;SW_A_Tamaño_Datos = 0;SW_A_Conjunto_datos = 0;SW_A_Formato_texto = 0

        # Ecuacion
        SW_Ecuacion = 0;SW_E_Repo = 0;SW_E_Plataforma = 0;SW_E_Sitio = 0;SW_E_Tipo_recurso = 0;SW_E_Tamaño_Datos = 0;SW_E_Conjunto_datos = 0;SW_E_Formato_texto = 0

        # SW Licencias
        SW_A_Licencia_Autorizacion = 0
        SW_A_Licencia_uso = 0
        SW_E_Licencia_Autorizacion = 0
        SW_E_Licencia_uso = 0
        SW_P_Licencia_Autorizacion = 0
        SW_P_Licencia_uso = 0
        SW_B_Licencia_Autorizacion = 0
        SW_B_Licencia_uso = 0

        # Datos Brutos
        SW_Datos_Brutos = 0;SW_B_Repo = 0;SW_B_Plataforma = 0;SW_B_Sitio = 0;SW_B_Tipo_recurso = 0;SW_B_Tamaño_Datos = 0;SW_B_Conjunto_datos = 0;SW_B_Formato_texto = 0

        # Datos Procesados
        SW_Datos_Procesados = 0;SW_P_Repo = 0;SW_P_Plataforma = 0;SW_P_Sitio = 0;SW_P_Tipo_recurso = 0;SW_P_Tamaño_Datos = 0;SW_P_Conjunto_datos = 0;SW_P_Formato_texto = 0


        # Variables De Porcentaje
        Total_Algoritmo = 0
        Total_Ecuaciones = 0
        Total_Datos_P = 0
        Total_Datos_B = 0

    
        # Abrir el archivo PDF
        with open(os.path.join(dir_path, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            stop_search = False

            for page in range(len(pdf_reader.pages)):
                page_text = pdf_reader.pages[page].extract_text().lower()
                
                # Detener Antes de llegar a Referencias
                if stop_search or page == len(pdf_reader.pages) - 2:
                    break
                page_text = pdf_reader.pages[page].extract_text().lower()
                

                # ** DETERMINAR CONTENIDO DEL ARTICULO [PDF] ** 


                # LICENCIA
                urls = re.findall(url_regex, page_text)
                if urls:
                    urls_encontrados.extend(urls)
                    for url in urls_encontrados:
                        for Lice in Licence:
                            if Lice.match(url):
                                SW_A_Licencia_Autorizacion = 1
                                SW_A_Licencia_uso = 1
                                SW_E_Licencia_Autorizacion = 1
                                SW_E_Licencia_uso = 1
                                SW_P_Licencia_Autorizacion = 1
                                SW_P_Licencia_uso = 1
                                SW_B_Licencia_Autorizacion = 1
                                SW_B_Licencia_uso = 1
                                break
                        break           
                

                # -Limpiar Variables-
                urls = ''
                urls_encontrados = []
                urls_repositorio = []

                # -------------------------------
                # ALGORITMO.
                if any(palabra in page_text for palabra in Algorith_Words):
                    urls = re.findall(url_regex, page_text)
                    SW_Algoritmo = 1

                    # Conjunto Datos / Tamaño Datos (Tablas, Imagenes, Grafos)
                    pdf_page = pdf_reader.pages[page]
                    if '/XObject' in pdf_page['/Resources']:
                        x_objects = pdf_page['/Resources']['/XObject'].get_object()
                        if x_objects:
                            for obj in x_objects:
                                if x_objects[obj]['/Subtype'] == '/Image':
                                    SW_A_Conjunto_datos = 1
                                    urls = re.findall(url_regex, page_text)
                                    if urls:
                                        SW_A_Conjunto_datos = 1
                                        SW_A_Tamaño_Datos = 1
                                        break
                    
                    # Plataforma / Sitio
                    if urls:
                        for Li in Licence:
                            if urls != Li:
                                SW_A_Plataforma = 1 
                                SW_A_Sitio = 1
                                urls_encontrados.extend(urls)
                        for url in urls_encontrados:
                            # Repositorio
                            for repo_regex in repositorio_regexes:
                                if repo_regex.match(url):
                                    SW_A_Repo = 1
                                    # Tipo de Recurso
                                    try:
                                        for url_A in repositorio_regexes:
                                            response = urllib.request.urlopen(url_A)
                                            content_type = response.headers.get('Content-Type')
                                            if content_type:
                                                mime_type, encoding = mimetypes.guess_type(url_A, strict=True)
                                                if mime_type:
                                                    SW_A_Tipo_recurso = 1
                                                    break
                                                else:
                                                    SW_A_Tipo_recurso = 0
                                            else:
                                                SW_A_Tipo_recurso = 0
                                    except:
                                        SW_A_Tipo_recurso = 0
                                    break  # Salir del bucle si se encuentra una coincidencia

                # -Limpiar Variables-
                urls = ''
                urls_encontrados = []
                urls_repositorio = []


                # --------------------------------
                # ECUACIONES / FORMULAS / TEOREMAS.
                #if sympy.preview(page_text, output='text'):
                if any(palabra in page_text for palabra in Ecuation_Patron):
                    SW_Ecuacion = 1
                    urls = re.findall(url_regex, page_text)

                    # Conjunto Datos / Tamaño Datos (Tablas, Imagenes, Grafos)
                    pdf_page = pdf_reader.pages[page]
                    if '/XObject' in pdf_page['/Resources']:
                        x_objects = pdf_page['/Resources']['/XObject'].get_object()
                        if x_objects:
                            for obj in x_objects:
                                if x_objects[obj]['/Subtype'] == '/Image':
                                    SW_A_Conjunto_datos = 1
                                    urls = re.findall(url_regex, page_text)
                                    if urls:
                                        SW_E_Conjunto_datos = 1
                                        SW_E_Tamaño_Datos = 1
                                        break
                    
                    if urls:
                        # Plataforma - Sito
                        for Li in Licence:
                            if urls != Li:
                                SW_A_Plataforma = 1 
                                SW_A_Sitio = 1
                                urls_encontrados.extend(urls)
                        for url in urls_encontrados:
                            # Repositorio
                            for repo_regex in repositorio_regexes:
                                if repo_regex.match(url):
                                    SW_E_Repo = 1
                                    # Tipo de Recurso
                                    try:
                                        for url_E in repositorio_regexes:
                                            response = urllib.request.urlopen(url_E)
                                            content_type = response.headers.get('Content-Type')
                                            if content_type:
                                                mime_type, encoding = mimetypes.guess_type(url_E, strict=True)
                                                if mime_type:
                                                    SW_E_Tipo_recurso = 1
                                                    break
                                                else:
                                                    SW_E_Tipo_recurso = 1
                                            else:
                                                SW_E_Tipo_recurso = 0
                                    except:
                                        SW_E_Tipo_recurso = 0
                                break
    

                # -Limpiar Variables-
                urls = ''
                urls_encontrados = []
                urls_repositorio = []


                # --------------------------------
                # DATOS PEOCESADOS.
                pdf_page = pdf_reader.pages[page]
                if '/XObject' in pdf_page['/Resources']:
                    x_objects = pdf_page['/Resources']['/XObject'].get_object()
                    if x_objects:
                        for obj in x_objects:
                            if x_objects[obj]['/Subtype'] == '/Image':
                                urls = re.findall(url_regex, page_text)
                                SW_Datos_Procesados = 1
                                if urls:
                                # Plataforma - Sito
                                    for Li in Licence:
                                        if urls != Li:
                                            urls_encontrados.extend(urls)
                                            SW_P_Sitio = 1
                                            SW_P_Plataforma = 1
                                            break
                                    for url in urls_encontrados:
                                        # Repositorio
                                        for repo_regex in repositorio_regexes:
                                            if repo_regex.match(url):
                                                SW_P_Repo = 1
                                                SW_P_Conjunto_datos = 1
                                                SW_P_Tamaño_Datos = 1
                                            # Tipo de Recurso
                                            try:
                                                for url_P in repositorio_regexes:
                                                    response = urllib.request.urlopen(url_P)
                                                    content_type = response.headers.get('Content-Type')
                                                    if content_type:
                                                        mime_type, encoding = mimetypes.guess_type(url_P, strict=True)
                                                        if mime_type:
                                                            SW_P_Tipo_recurso = 1
                                                            break
                                                        else:
                                                            SW_P_Tipo_recurso = 1
                                                    else:
                                                        SW_P_Tipo_recurso = 0
                                            except:
                                                SW_P_Tipo_recurso = 0
                                        break


                # -Limpiar Variables-
                url = ''
                urls = ''
                urls_encontrados = []
                urls_repositorio = []


                # --------------------------------
                # DATOS BRUTOS. 
                page_obj = pdf_reader.pages[page]
                page_text = page_obj.extract_text()
                for char in page_text:
                    if ord(char) > 127:
                        SW_Datos_Brutos = 1
                        urls = re.findall(url_regex, page_text)
                        if urls:
                            # Plataforma - Sito
                            for Li in Licence:
                                if urls != Li:
                                    SW_B_Plataforma = 1 
                                    SW_B_Sitio = 1
                                    urls_encontrados.extend(urls)
                                    break
                                for url in urls_encontrados:
                                    # Repositorio
                                    for repo_regex in repositorio_regexes:
                                        if repo_regex.match(url):
                                            SW_B_Repo = 1
                                            SW_B_Conjunto_datos = 1
                                            SW_B_Tamaño_Datos = 1
                                        # Tipo de Recurso
                                        try:
                                            for url_B in repositorio_regexes:
                                                response = urllib.request.urlopen(url_B)
                                                content_type = response.headers.get('Content-Type')
                                                if content_type:
                                                    mime_type, encoding = mimetypes.guess_type(url_B, strict=True)
                                                    if mime_type:
                                                        SW_B_Tipo_recurso = 1
                                                        break
                                                    else:
                                                        SW_B_Tipo_recurso = 1
                                                else:
                                                    SW_B_Tipo_recurso = 0
                                        except:
                                            SW_B_Tipo_recurso = 0
                                    break
            """

############################################################################
        #EXAMINANDO REPRODUCIBILIDAD VER. 2.0 - EXTRAYENDO LOS DATASETS Y ANALIZANDO EL CONTENIDO DE ESTE

    
        # DETECTAR ECUACION (En el PDF)
        SW_Ecuacion_PDF = 0
        with open(pdf_path, 'rb') as archivo_pdf:
            pdf_reader = PdfReader(archivo_pdf)
            num_palabras_encontradas = 0

            for pagina in pdf_reader.pages:
                texto_pagina = pagina.extract_text().lower()

                for palabra in Ecuation_Words:
                    if palabra.lower() in texto_pagina:
                        num_palabras_encontradas += 1

                        if num_palabras_encontradas >= 1:
                            SW_Ecuacion_PDF = 1
                            break

                if num_palabras_encontradas >= 2:
                    break

                if "References" in texto_pagina:
                    break
        #print("ECUACION PDF: ", SW_Ecuacion_PDF,"\n")
        

        Doc = fitz.open(pdf_path)
    
        # Lista - Extraer los enlaces de descarga /.zip y otros
        All_In_Url = []
        # Lista Para extraer Links Normales - Sitio / Plataforma 
        All_In_Url_S_P = []

        Urls_antes_referencias = []
        Urls_despues_referencias = []

        # Lista de url visitadas
        urls_visitadas = set()

        # VARIABLES REPRODUCIBILIDAD:
        SW_ALGORITMO = 0
        SW_ECUACION = 0
        SW_DATA = 0

        # Buscar por texto para sitio/plataformas que requieran autentificacion.
        SW_ALGORITMO_TEXT = 0
        SW_DATA_TEXT = 0
        Tipo_Data_Text = ''
        Tipo_Code_Text = ''

        SW_Repositorio = 0
        SW_Plataforma = 0
        SW_Sitio = 0
        SW_Sitio_Plataforma = 0

        SW_Tamaño_Datos = 0                 #DEPENDE DE TIPO DE RECURSO

        SW_Licence_Uso = 0
        SW_Licence_Autorizacion = 0         #DEPENDE DE LICENCIA DE USO

        SW_Conjunto_Datos = 0               #SI EXISTEN DATOS

        SW_Formato_Texto = 0                #DEPENDE DE TIPO RECURSO

        Tipo_Code = ''
        Tipo_Data = ''
        
        
        #EQUIVALENTE PROCENTAJE
        Elementos = 0
        REPRO_ACOMULADO = 0
        Equiv_Algoritmo = 23.2404
        Equiv_Ecuacion = 7.2762
        Equiv_Datos_B = 21.8286
        Equiv_Datos_P = 1.9548
    

        #EXTRAER URL
        for i in range(Doc.page_count - 1):
            page = Doc.load_page(i)

            # METODO 1 (fitz) - URL_HIPERTEXTO
            Url_Hipertexto = page.get_links()
            for link in Url_Hipertexto:
                url = link.get("uri", "")
                #print("LINKS: ", url)
                if any(regex.match(url) for regex in Gestor_Bibliographi):
                    Url_Repo.append(url)
                    SW_Repositorio = 1
                else:
                    #Para Excluir url
                    if any(regex.match(url) for regex in Gestor_Exclu):
                        Url_Excl.append(url)
                    else:
                        #ES SITIO/PLATAFORMA
                        Url_Normal.append(url)
                        

            # METODO 2 (fitz) - URL
            text = page.get_text()
            Url = re.findall(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+!*\'(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', text)
            for url in Url:
                if verificar_url(url):
                    if any(normal.match(url) for normal in Gestor_Bibliographi):
                        Url_Repo.append(url)
                        SW_Repositorio = 1
                        
                    else:
                        #Para Excluir url
                        if any(regex.match(url) for regex in Gestor_Exclu):
                            Url_Excl.append(url)
                        else:
                            #ES SITIO/PLATAFORMA
                            Url_Normal.append(url)
                            

            if ("References" in text or "REFERENCES" in text):
                break
            if ("References" in Url_Hipertexto or "REFERENCES" in Url_Hipertexto):
                break
        
        # Cerrar el archivo PDF
        Doc.close()

        #///// validando referencias - TESTING 
        """
        ultimas_paginas = Doc.page_count - 5
        if ultimas_paginas < 0:
            ultimas_paginas = 0

        for i in range(Doc.page_count - 1):
            page = Doc.load_page(i)

            # METODO 1 (fitz) - URL_HIPERTEXTO
            Url_Hipertexto = page.get_links()
            for link in Url_Hipertexto:
                url = link.get("uri", "")
                #print("LINKS: ", url)
                if any(regex.match(url) for regex in Gestor_Bibliographi):
                    Url_Repo.append(url)
                    SW_Repositorio = 1
                else:
                    #Para Excluir url
                    if any(regex.match(url) for regex in Gestor_Exclu):
                        Url_Excl.append(url)
                    else:
                        #ES SITIO/PLATAFORMA
                        Url_Normal.append(url)
                        SW_Sitio_Plataforma = 1
                        
            if i >= ultimas_paginas:
                # METODO 2 (fitz) - URL
                text = page.get_text()
                Url = re.findall(r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+!*\'(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)', text)

                en_pagina_referencias = False  # Variable para controlar si se encuentra en la página de referencias

                # Obtener las últimas 5 páginas del documento
                ultimas_paginas = Doc.get_page_count() - 5
                if ultimas_paginas < 0:
                    ultimas_paginas = 0

                for page_num in range(Doc.get_page_count()):
                    if page_num >= ultimas_paginas:
                        page = Doc.load_page(page_num)
                        page_text = page.get_text()

                        # Verificar si la página contiene la palabra "References"
                        if "References" in page_text or "REFERENCES" in page_text:
                            en_pagina_referencias = True
                            break

                for url in Url:
                    if verificar_url(url):
                        if any(normal.match(url) for normal in Gestor_Bibliographi):
                            Url_Repo.append(url)
                            SW_Repositorio = 1
                        else:
                            if any(regex.match(url) for regex in Gestor_Exclu):
                                Url_Excl.append(url)
                            else:
                                # ES SITIO/PLATAFORMA
                                if en_pagina_referencias:
                                    Urls_despues_referencias.append(url)
                                else:
                                    Urls_antes_referencias.append(url)
                                SW_Sitio_Plataforma = 1

                # Verificar las URLs encontradas antes de "References"
                print("URLs encontradas antes de 'References':")
                for url in Urls_antes_referencias:
                    print(url)

                # Verificar las URLs encontradas después de "References"
                print("URLs encontradas después de 'References':")
                for url in Urls_despues_referencias:
                    print(url)"""

        # Eliminando Duplicadas - Metodo fitz
        Url_Normal = list(set(Url_Normal))
        Url_Repo = list(set(Url_Repo))

        """  RESULTADOS  URL """
        """ ***************************** """
        # Urls Sitio/Plataforma
        #print("URLs Normales:")
        #for url_n in Url_Normal:
            #print(url_n)

        # Urls repositorios
        #print("\n")
        #print("URLs Repositorios:")
        #for url_r in Url_Repo:
            #print(url_r)
        #print("\n")    
        """ ***************************** """


        """     # SCRAPING WEB #     """
        #Config Chrome
        #service = Service(ChromeDriverManager().install())
        #options = webdriver.ChromeOptions()
        #options.headless = False
        #options.add_argument('--headless')
        #driver = webdriver.Chrome(service=service, options=options)
        #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        #options.add_argument('--headless')

        options = Options()
        options.headless = False
        #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver = webdriver.Chrome(options=options)


        #------------------------------------------------------------------------------------------------------
        # *-*-*-*- PARA LAS URL REPOSITORIOS ENCONTRADAS EN EL PDF
        if SW_Repositorio == 1:
            for url_r in Url_Repo:
                url_base = url_r

                driver.get(url_base)

                load_more = True
                for i in range(10):
                    time.sleep(0.5)#0.5
                    try:
                        load_more_btn = driver.find_element(By.XPATH, '/html/body/div[2]/section/div[2]/div/div[3]/div/a')
                        load_more_btn.click()
                    except:
                        load_more = False
                
                #BUSCAR TEXTO LICENSE
                if SW_Licence_Uso != 1:
                    body_element = driver.find_element(By.TAG_NAME, 'body')
                    for search in Texto_License:
                        if search in body_element.text:
                            #print(f"Texto encontrado: {search}")
                            SW_Licence_Uso = 1
                            SW_Licence_Autorizacion = 1
                            break

                #BUSCAR LINKS
                links = driver.find_elements(By.XPATH, "//a[@href]")

                #EXTRAER TODOS LOS URL INTERNOS CON EXTENSIONES ".COMPRIMIDO"/ DESCARGA
                for link in links:
                    href = link.get_attribute("href")

                    #print("HREF: ", href)

                    # Si el link es .zip o de descarga.
                    #if href.endswith('.zip') or ('download' in href) or ('zip' in href):
                    # or (('dataset' in href) and ('file' in href))
                    if href.endswith('.zip') or ('download' in href) or ('zip' in href) or href.endswith('.tar') or href.endswith('.gz') or href.endswith('.tar.gz') or href.endswith('.bz2') or href.endswith('.tar.bz2') or href.endswith('.rar') or (('dataset' in href) and ('file' in href)):
                        All_In_Url.append(href)
                        SW_Conjunto_Datos = 1
                        if href.endswith('.zip'):
                            break

                    #AUTENTICACION - ELSEVIER
                    body_element = driver.find_element(By.TAG_NAME, 'body')
                    if "Introduzca su dirección de correo electrónico para continuar con Digital Commons Data" in body_element.text:
                        try:
                            response = requests.get(href)
                            if response.status_code == 401 or  response.status_code == 403:
                                #Colocar Correo
                                email_input = driver.find_element(By.ID, "bdd-email")
                                email_input.send_keys("torresjosej@americana.edu.co")

                                #Dar click en CONTINUAR
                                continue_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
                                continue_button.click()

                                #Colocar contraseña
                                password_input = driver.find_element(By.ID, "bdd-password")
                                password_input.send_keys("Elsevier1450065!!")

                                #Iniciar sesion
                                login_button = driver.find_element(By.ID, "bdd-elsPrimaryBtn")
                                login_button.click()

                                links = driver.find_elements(By.XPATH, "//a[@href]")

                                for link in links:
                                    href = link.get_attribute("href")

                                    # Si el link es .zip o de descarga.
                                    #if href.endswith('.zip') or ('download' in href) or ('zip' in href):
                                    if href.endswith('.zip') or ('download' in href) or ('zip' in href) or href.endswith('.tar') or href.endswith('.gz') or href.endswith('.tar.gz') or href.endswith('.bz2') or href.endswith('.tar.bz2') or href.endswith('.rar') or (('dataset' in href) and ('file' in href)):
                                        All_In_Url.append(href)
                                        SW_Conjunto_Datos = 1
                                break
                        except:
                            continue
            driver.quit()

            # Limpiar Repetidos
            All_In_Url = list(set(All_In_Url))

            #print(All_In_Url)

            # -*-*-*-*- EVALUAR RECURSOS Y ELEMENTOS PARA REPOSITORIOS
            for url in All_In_Url:
                if url not in urls_visitadas:
                    try:
                        response = requests.get(url)
                        content = response.text

                        print("Buscando en: ", url)
                        #print("CONTENIDO: ",content)

                        #Primera Busqueda. CODE/AGORITMO - DATA
                        if SW_ALGORITMO != 1:
                            for ext in Extension_Code:
                                #if ext in content or content.endswith(ext):
                                if ext in content:
                                    Tipo_Code = ext
                                    #print("Code found - Paso 2:", url)
                                    #print("Extensión encontrada:", Tipo_Code)
                                    SW_ALGORITMO = 1
                                    SW_Tamaño_Datos = 1
                                    SW_Formato_Texto = 1                            
                                    break
                        
                        
                        if SW_DATA != 1:
                            for data in Extensions_Data:
                                #if data in content or content.endswith(ext):
                                if data in content:
                                    Tipo_Data = data
                                    #print("Data found - Paso 2:", url)
                                    #print("Extensión encontrada:", Tipo_Data)
                                    SW_DATA = 1
                                    SW_Tamaño_Datos = 1
                                    SW_Formato_Texto = 1 
                                    break

                        urls_visitadas.add(url)
                    except requests.exceptions.RequestException as e:
                        urls_visitadas.add(url)
                        print(f"Error al acceder a {url}: {str(e)}")
        
        #------------------------------------------------------------------------------------------------------
        # *-*-*-*-* PARA LAS URL SITIO / PLATAFORMA ENCONTRADAS EN EL PDF. AQUI SE DETERMINA SI ES SITIO/PLATAFORMA.

        #Config Chrome
        options = Options()
        options.headless = False
        #options.add_argument('--headless')
        
        if SW_Repositorio == 0:
            for url_S_P in Url_Normal:
                try:    
                    url_base = url_S_P
                    print("Buscando en: ", url_S_P,"\n")
                    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                    driver.get(url_S_P)

                    load_more = True
                    for i in range(10):
                        time.sleep(0.5)
                        try:
                            load_more_btn = driver.find_element(By.XPATH, '/html/body/div[2]/section/div[2]/div/div[3]/div/a')
                            load_more_btn.click()
                        except:
                            load_more = False

                    #BUSCAR TEXTO LICENCIA
                    if SW_Licence_Uso != 1:
                        body_element = driver.find_element(By.TAG_NAME, 'body')
                        for search in Texto_License:
                            if search in body_element.text:
                                #print(f"Licencia encontrado: {search}")
                                SW_Licence_Uso = 1
                                SW_Licence_Autorizacion = 1
                                break

                    #BUSCAR TEXTO SITIO - PLATAFORMA
                    if SW_Sitio_Plataforma != 1 :
                        body_element = driver.find_element(By.TAG_NAME, 'body')
                        for search in Texto_Sitio_Plataforma:
                            if search in body_element.text:
                                #print(f"Sitio/Plataforma encontrado: {search}")
                                SW_Plataforma = 1
                                #SW_Sitio_Plataforma = 1
                                break
                        if SW_Plataforma != 1:
                            SW_Sitio = 1
                            #SW_Sitio_Plataforma = 1

                    
                    #BUSCANDO TIPO DE DATA/CODE POR TEXTO
                    if SW_ALGORITMO_TEXT != 1:
                        for ext in Extension_Code:
                            body_element = driver.find_element(By.TAG_NAME, 'body')
                            if ext in body_element.text:
                                SW_ALGORITMO_TEXT = 1
                                Tipo_Code_Text = ext
                                print("Code encontrado en texot: ",Tipo_Code_Text)
                                if SW_Plataforma == 1:
                                    SW_Sitio_Plataforma = 1
                                if SW_Sitio == 1:
                                    SW_Sitio_Plataforma = 1
                                break 
                                
                    if SW_DATA_TEXT != 1:
                        for data in Extensions_Data:
                            body_element = driver.find_element(By.TAG_NAME, 'body')
                            if data in body_element.text:
                                SW_DATA_TEXT = 1
                                Tipo_Data_Text = data
                                print("Data encontrado en texot: ",Tipo_Data_Text)
                                if SW_Plataforma == 1:
                                    SW_Sitio_Plataforma = 1
                                if SW_Sitio == 1:
                                    SW_Sitio_Plataforma = 1 
                                break
                            

                    #BUSCAR LINKS
                    links = driver.find_elements(By.XPATH, "//a[@href]")

                    #EXTRAER TODOS LOS URL INTERNOS CON EXTENSIONES ".COMPRIMIDO"/ DESCARGA
                    for link in links:
                        href = link.get_attribute("href")

                        # Si el link es .zip o de descarga.
                        #if href.endswith('.zip') or ('download' in href) or ('zip' in href):
                        if (href.endswith('.zip')) or (('download' in href and 'zip' in href)) or ('zip' in href) or (href.endswith('.tar')) or (href.endswith('.gz')) or (href.endswith('.tar.gz')) or (href.endswith('..bz2')) or (href.endswith('.tar.bz2')) or (href.endswith('.rar')) or (('dataset' in href and 'file' in href)) or (('dataset' in href and 'download' in href)):

                            All_In_Url.append(href)
                            #print("URL ZIP/DOWNLOAD", All_In_Url,"\n")
                            SW_Conjunto_Datos = 1

                            #SI ENCONTRO ARCHIVOS EN EL SITIO/PLATAFORMA
                            if SW_Plataforma == 1:
                                SW_Sitio_Plataforma = 1
                            if SW_Sitio == 1:
                                SW_Sitio_Plataforma = 1

                        # si es una pagina
                        #if href.startswith(url_base):
                            #All_In_Url_S_P.append(href)

                    driver.quit()

                    # Limpiar Repetidos
                    All_In_Url = list(set(All_In_Url))
                    #All_In_Url_S_P = list(set(All_In_Url_S_P))

                    
                    for url in All_In_Url:        # Evaluando links de ".Comprimido" de Ulrs de Siti/Plataforma
                        if url not in urls_visitadas:
                            try:
                                response = requests.get(url)
                                content = response.text

                                #print("Buscando en (URL CAPTADAS CON SELENIUM EN URL_NORMALES): ", url)
                                #print("CONTENIDO: ", content)

                                #Primera Busqueda. CODE/AGORITMO - DATA
                                if SW_ALGORITMO != 1:
                                    for ext in Extension_Code:
                                        if (ext in content) and ('html' not in content):
                                            Tipo_Code = ext
                                            #print("Code found in Sitio/Platadorma - Paso 2:", url)
                                            #print("Extensión encontrada:", Tipo_Code)
                                            SW_ALGORITMO = 1
                                            SW_Tamaño_Datos = 1
                                            SW_Formato_Texto = 1

                                            #SI ENCONTRO ARCHIVOS EN EL SITIO/PLATAFORMA
                                            if SW_Plataforma == 1:
                                                SW_Sitio_Plataforma = 1
                                            if SW_Sitio == 1:
                                                SW_Sitio_Plataforma = 1                            
                                            break
                                
                                
                                if SW_DATA != 1:
                                    for data in Extensions_Data:
                                        if (data in content) and ('html' not in content):
                                            Tipo_Data = data
                                            #print("Data found in Sitio/Platadorma - Paso 2:", url)
                                            #print("Extensión encontrada:", Tipo_Data)
                                            SW_DATA = 1
                                            SW_Tamaño_Datos = 1
                                            SW_Formato_Texto = 1 

                                            #SI ENCONTRO ARCHIVOS EN EL SITIO/PLATAFORMA
                                            if SW_Plataforma == 1:
                                                SW_Sitio_Plataforma = 1
                                            if SW_Sitio == 1:
                                                SW_Sitio_Plataforma = 1
                                            break

                                urls_visitadas.add(url)
                            except requests.exceptions.RequestException as e:
                                urls_visitadas.add(url) 
                                #print(f"Error al acceder a {url}: {str(e)}")
                    
                except:
                    #print("URL INVALIDA: ", url_S_P,"\n")
                    urls_visitadas.add(url_S_P)
                    continue


            # Si encontro Extension por texto y no por contenido:
            if SW_ALGORITMO != 1 and SW_ALGORITMO_TEXT != 0:
                #print("FILTRO CODE OK")
                SW_ALGORITMO = 1
                Tipo_Code = Tipo_Code_Text
                SW_Conjunto_Datos = 1
                SW_Tamaño_Datos = 1
                SW_Formato_Texto = 1

            if SW_DATA != 1 and SW_DATA_TEXT != 0:
                #print("FILTRO DATA OK","\n")
                SW_DATA = 1
                Tipo_Data = Tipo_Data_Text
                SW_Conjunto_Datos = 1
                SW_Tamaño_Datos = 1
                SW_Formato_Texto = 1

        #determinar Ecuacion
        if SW_Ecuacion_PDF == 1 and SW_DATA == 1:
            SW_ECUACION = 1
        
        # CALCULAR EQUIVALENTE
        if SW_ALGORITMO == 1:
            REPRO_ACOMULADO = REPRO_ACOMULADO + Equiv_Algoritmo
        if SW_DATA == 1:
            REPRO_ACOMULADO = REPRO_ACOMULADO + Equiv_Datos_B + Equiv_Datos_P
        if SW_ECUACION == 1:
            REPRO_ACOMULADO = REPRO_ACOMULADO + Equiv_Ecuacion


        REPRO_ACOMULADO_FINAL = REPRO_ACOMULADO
        
        if SW_Repositorio == 1:
            Elementos += 1
        if SW_Sitio_Plataforma == 1:
            Elementos += 1
        if SW_Tamaño_Datos == 1:
            Elementos += 1
        if SW_Licence_Uso == 1:
            Elementos += 1
        if SW_Licence_Autorizacion == 1:
            Elementos += 1
        if SW_Conjunto_Datos == 1:
            Elementos += 1
        if SW_Formato_Texto == 1:
            Elementos += 1

        
        
        # FILTRO CALCULO Y [SITIO/PLATAFORMA - REPOSITORIO]
        #SW_Repositorio == 0 or SW_Sitio_Plataforma == 0 or
        try:
            if SW_Tamaño_Datos == 0 or SW_Licence_Uso == 0 or SW_Licence_Autorizacion == 0 or SW_Conjunto_Datos == 0 or SW_Formato_Texto == 0:

                #if SW_Repositorio == 0 and SW_Sitio_Plataforma == 1:

                #if SW_Repositorio == 1 and SW_Sitio_Plataforma == 0:
                    
                #if SW_Repositorio == 0 and SW_Sitio_Plataforma == 1:

                if SW_Repositorio == 1 and SW_Sitio_Plataforma == 1:
                    Elementos = Elementos - 1

                REPRO_ACOMULADO = REPRO_ACOMULADO / Elementos
                REPRO_ACOMULADO_FINAL = REPRO_ACOMULADO_FINAL - REPRO_ACOMULADO
        except:
           REPRO_ACOMULADO_FINAL = REPRO_ACOMULADO_FINAL


        #print("ELEMENTOS: ", Elementos)

        # METADATA DATASET
        if SW_Conjunto_Datos == 1 :
            datasetSW = 1
            ValueDataset = valueVisi


        # RESULTADOS   
        print("*** REPRODUCIBILIDAD %:", REPRO_ACOMULADO_FINAL)
        print("ALGORITMO: ", SW_ALGORITMO)
        print("ECUACIONES: ", SW_ECUACION)
        print("DATOS: ", SW_DATA)

        print("Repositorio: ", SW_Repositorio)

        if SW_Sitio_Plataforma == 1:
            if SW_Plataforma == 1:
                print("Plataforma", SW_Plataforma)                
            else:
                print("Sitio", SW_Sitio)
        else:
            print("Sitio/Plataforma ", SW_Sitio_Plataforma)

        print("Tamaño Datos: ", SW_Tamaño_Datos)

        print("Licencia Uso: ", SW_Licence_Uso)
        print("Licencia Autorizacion: ", SW_Licence_Autorizacion)

        print("Conjunto Datos: ", SW_Conjunto_Datos)
        print("Formato Texto: ", SW_Formato_Texto,"\n")


        # 1. ACCESIBILIDAD 
        PorcentajeVisibilidad = ValueOpenAccess+Valuerestringed+ValueOnlyMetadata+ValueFullText+ValueDataset+ValueSoftware+ValueEmbargado

        PorcentajeMetadatos = ValueAuthor+ValueTitle+ValueYear+ValueKeyword+ValueIssn+ValueAbstract+ValueLink+ValueDoi+ValueUri+ValueUrl+ValueVersion+ValueImagen

        PorcentajeEditorial = ValueOpenAccessTotal+Valuedownload+ValueparcialAccess+ValueSubscribe

        accesibilidad = PorcentajeVisibilidad + PorcentajeMetadatos + PorcentajeEditorial

        Rango_Doc_Normal = ''
        Rango_Doc_Cambiados = ''
        Rango_Doc_Cambiados_New = ''


        # RANGO - TOTAL DOCUMENTO - VALORES NORMALES
        Total_Valor_Doc = 0
        Total_Valor_Doc = accesibilidad + Contenidos + REPRO_ACOMULADO_FINAL
        if Total_Valor_Doc >=0 and Total_Valor_Doc <= 34.99:
            Rango_Doc_Normal = "MALO"
        if Total_Valor_Doc >=35 and Total_Valor_Doc <= 69.99:
            Rango_Doc_Normal = "REGULAR"
        if Total_Valor_Doc >=70:
            Rango_Doc_Normal = "BUENO"


        # VALORES CAMBIADOS 
        if Total_Valor_Doc >=0 and Total_Valor_Doc <= 24.99:
            Rango_Doc_Cambiados = "MALO"
        if Total_Valor_Doc >=25 and Total_Valor_Doc <= 49.99:
            Rango_Doc_Cambiados = "REGULAR"
        if Total_Valor_Doc >=50:
            Rango_Doc_Cambiados = "BUENO"

        # VALORES CAMBIADOS_NEW 
        if Total_Valor_Doc >=0 and Total_Valor_Doc <= 30.99:
            Rango_Doc_Cambiados_New = "MALO"
        if Total_Valor_Doc >=31 and Total_Valor_Doc <= 59.99:
            Rango_Doc_Cambiados_New = "REGULAR"
        if Total_Valor_Doc >=60:
            Rango_Doc_Cambiados_New = "BUENO"


        #///////////////////////////////////////////////////////////////////////////////////////////////////
        """EXPORTAR SALIDA A EXCEL"""
        
        # Diccionarios:
        
        H_Resultados = {
            'DOI': [Doi],
            'NOMBRE': [Nombre],
            'ACCESIBILIDAD': ["{0:.4f}".format(accesibilidad)],
            'CONTENIDOS': ["{0:.4f}".format(Contenidos)],
            'REPRODUCIBILIDAD': ["{0:.4f}".format(REPRO_ACOMULADO_FINAL)],
            'VALOR': ["{0:.4f}".format(Total_Valor_Doc)],
            'CATEGORIA NORMAL': [Rango_Doc_Normal],
            'CATEGORIA CAMBIADOS': [Rango_Doc_Cambiados],
            'CATEGORIA CAMBIADOS_NEW': [Rango_Doc_Cambiados_New]

        }
        
        H_Accesibilidad = {
            'DOI': [Doi],
            'NOMBRE': [Nombre],
            'Acceso Abierto': [accesoabiertoSW],
            'Acceso Embargado': [ValueEmbargado],
            'Acceso Restringido': [restringedSW],
            'Solo Metadatos': [onlymetadataSW],
            'Full Text': [fulltextSW],
            'Dataset': [datasetSW],
            'Software': [softwareSW],
            'Nombre Autor': [autorSW],
            'Titulo': [tituloSW],
            'Año': [yearSW],
            'Keyword': [keywordSW],
            'C. Code': [IssnSW],
            'Resumen': [abstractSW],
            'Enlaces': [linkSW],
            'Multimedias': [imagenSW],
            'Doi': [DoiSW],
            'Url': [urlSW],
            'Uri': [uriSW],
            'Version': [versionSW],
            'Acceso Abierto Total': [openAccessTotalSW],
            'Pago Por Descarga': [downloadSW],
            'Acceso Parcial': [parcialAccessSW],
            'Por Suscripcion': [SubscribeSW],
            '% Visibilidad %': ["{0:.4f}".format(PorcentajeVisibilidad)],
            '% Contenido %': ["{0:.4f}".format(PorcentajeMetadatos)],
            '% P. Editorial %': ["{0:.4f}".format(PorcentajeEditorial)],

            'TOTAL ACCESIBILIDAD': ["{0:.4f}".format(accesibilidad)],

        }

        H_Contenidos = {
            'DOI': [Doi],
            'NOMBRE': [Nombre],
            'Densidad Lexica': ["{0:.5f}".format(Densidad_Lexica)],
            'Complejidad Oracion': ["{0:.5f}".format(Nor_Complejidad_Oracion_Peso)],
            'Complejidad Sintáctica': ["{0:.5f}".format(Norm_Complejidad_Sintactica_Peso)],
            'Marcas De Puntuacion': ["{0:.5f}".format(Norm_Marcas_Puntuacion_Peso)],
            'Indice SSR': ["{0:.5f}".format(Norm_ssr_Peso)],
            'Facilidad De Lectura': ["{0:.5f}".format(Norm_Facilidad_Lectura_Peso)],
            'Arbol Sintaxis': ["{0:.5f}".format(Densidad_Arbol)],
            'Grado De Cumplimiento': ["{0:.5f}".format(Norm_Grado_Cumplimiento_Peso)],
            'Profundidad De Secciones': ["{0:.5f}".format(Norm_Profundidad_Secciones_Peso)],  

            '% Comprensibilidad %': ["{0:.5f}".format(TotalComprensibilidad)],
            '%. Legibilidad %': ["{0:.5f}".format(TotalLegibilidad)],
            '%. Esctru. Contenido %': ["{0:.5f}".format(TotalContenidos)],

            'TOTAL CONTENIDO': ["{0:.5f}".format(Contenidos)]
        }
        
        H_Reproducibilidad = {
            'DOI': [Doi],
            'NOMBRE': [Nombre],  
            'ALGORITMO': ["{0:.4f}".format(SW_ALGORITMO)],
            'ECUACIONES': ["{0:.4f}".format(SW_ECUACION)],
            'DATOS PROCESADOS': ["{0:.4f}".format(SW_DATA)],
            'DATOS BRUTOS': ["{0:.4f}".format(SW_DATA)],

            'TOTAL REPRODUCIBILIDAD': ["{0:.4f}".format(REPRO_ACOMULADO_FINAL)],
        }

        H_Repro_Detalles = {
            'DOI': [Doi],
            'NOMBRE': [Nombre],
            'Repositorio': [SW_Repositorio],
            'Plataforma': [SW_Plataforma],
            'Sitio': [SW_Sitio],
            'Tamaño Datos': [SW_Tamaño_Datos],
            'Licensia Uso': [SW_Licence_Uso],
            'Lic. Autorizacion': [SW_Licence_Autorizacion],
            'Conjunto Datos': [SW_Conjunto_Datos],
            'Formato Texto': [SW_Formato_Texto],

            'Tipo Recurso Data': [Tipo_Data],
            'Tipo Recurso Algoritmo': [Tipo_Code],
        }

        # DataFrames
        df1 = pd.DataFrame(H_Resultados)
        df2 = pd.DataFrame(H_Accesibilidad)
        df3 = pd.DataFrame(H_Contenidos)
        df4 = pd.DataFrame(H_Reproducibilidad)
        df5 = pd.DataFrame(H_Repro_Detalles)

        # Por si ya existe el Excel - Se le añade los nuevos datos
        try:
            with pd.ExcelFile("D:/JOSE/Otros/Algorithm Automation/Results/Results.xlsx", engine="openpyxl") as xls:
                df_existente1 = pd.read_excel(xls, sheet_name="RESULTADOS")
                df_existente2 = pd.read_excel(xls, sheet_name="ACCESIBILIDAD")
                df_existente3 = pd.read_excel(xls, sheet_name="CONTENIDOS")
                df_existente4 = pd.read_excel(xls, sheet_name="REPRODUCIBILIDAD")
                df_existente5 = pd.read_excel(xls, sheet_name="REPRO. DETALLES")

                

            df1 = pd.concat([df_existente1, df1], ignore_index=True)
            df2 = pd.concat([df_existente2, df2], ignore_index=True)
            df3 = pd.concat([df_existente3, df3], ignore_index=True)
            df4 = pd.concat([df_existente4, df4], ignore_index=True)
            df5 = pd.concat([df_existente5, df5], ignore_index=True)


        except FileNotFoundError:
            pass

        # Escribir en archivo de Excel
        writer = pd.ExcelWriter("D:/JOSE/Otros/Algorithm Automation/Results/Results.xlsx", engine="openpyxl")

        # DataFrames actualizados en sus respectivas hojas
        df1.to_excel(writer, sheet_name="RESULTADOS", index=False)
        df2.to_excel(writer, sheet_name="ACCESIBILIDAD", index=False)
        df3.to_excel(writer, sheet_name="CONTENIDOS", index=False)
        df4.to_excel(writer, sheet_name="REPRODUCIBILIDAD", index=False)
        df5.to_excel(writer, sheet_name="REPRO. DETALLES", index=False)


        # Guardar
        writer.close()

        
        # Limpiar Listas
        Url_Normal = []
        Url_Repo = []

        # Romper el jodido Ciclo
        #break


############################################################################
        
#///////////////////////////////////////////////////////////////////////////////////////////////////
        """EXPORTAR SALIDA A EXCEL"""
        

        # IMPRIMIR EN PANTALLA
        #   ////////////////////////-- 1. ACCESIBILIDAD --////////////////////////////////////////////
        """
        print("\n")
        print("////////////////////////////////////////////////////////////////////")
        print("DOI: ", Doi)
        print(f"Documento: {filename}","\t")
        print("METADATOS DE VISIBILIDAD:","\t","\t",("{0:.1f}".format(PorcentajeVisibilidad)))
        print("\t","Acceso Abierto:","\t", accesoabiertoSW)
        print("\t","Acceso Restringido:","\t", restringedSW)
        print("\t","Embargado:","\t","\t", embargadoSW)
        print("\t","Solo Metadatos:","\t", onlymetadataSW)
        print("\t","Full Text:","\t","\t", fulltextSW)
        print("\t","Dataset:","\t","\t", datasetSW)
        print("\t","Software:","\t","\t", softwareSW,"\n")

        print("METADATOS DE CONTENIDO:","\t","\t",("{0:.1f}".format(PorcentajeMetadatos)))
        print("\t","Nombre Autor:","\t","\t", autorSW)
        print("\t","Titulo:","\t","\t", tituloSW)
        print("\t","Año:","\t","\t","\t", yearSW)
        print("\t","Keyword:","\t","\t", keywordSW)
        print("\t","C. Code:","\t","\t", IssnSW)
        print("\t","Resumen:","\t","\t", abstractSW)
        print("\t","Enlaces:","\t","\t", linkSW)
        print("\t","Obetos Multimedias:","\t", imagenSW)
        print("\t","Doi:","\t","\t","\t", DoiSW,) 
        print("\t","Url:","\t","\t","\t", urlSW,)
        print("\t","Uri:","\t","\t","\t", uriSW,)
        print("\t","Version:","\t","\t", versionSW,"\n")

        print("METADATOS POLITICA EDITORIAL:","\t","\t",("{0:.1f}".format(PorcentajeEditorial)))
        print("\t","Acceso Abierto Total:","\t", openAccessTotalSW,)
        print("\t","Pago Por Descarga:","\t", downloadSW)
        print("\t","Acceso Parcial:","\t", parcialAccessSW)
        print("\t","Por Suscripcion:","\t", SubscribeSW,"\n")
        
        print("________________________")
        print("PORCENTAJE: ", ("{0:.1f}".format(PorcentajeTotal)))
        print("________________________","\n")
        """

        #   ////////////////////////-- 2. CONTENIDOS --//////////////////////////////////////////////
        """
        print("\n")
        print("1. COMPRENSIBILIDAD:")
        print("\t","* Densidad lexica: ", ("{0:.1f}".format(densidad_lexica)),"%")
        print("\t","* Frecuencia De Uso: ","\n")

        print("\t","* Complejidad De La Oracion: ")
        print("\t","\t",f"→ Longitud Oracional: {indice_longitud_oracional:.2f}")
        print("\t","\t",f"→ N. Frases Complejas: {cant_frases_complejas:.2f}","\n")

        print("\t","* Complejidad sintáctica:")
        print("\t","\t",f"→ Longitud De Oracion: ", abstract_length)
        print("\t","\t",f"→ Cantidad de Modificadores: ", num_modifiers,"\n")

        print("\t","* Marcas De Puntuacion: ", ("{0:.1f}".format(Sig_Puntuacion)),"\n")

        print("3. LEGIBILIDAD:")
        print("\t",f"* SSR: {result_SSR_Final:.2f}  ","||  Tipo: ", rangoSSR)
        print("\t","Facilidad De Lectura:")
        print("\t","\t",f"→ Varianza Coleman-Liau: {varianzaColeman:.2f}")
        print("\t","\t",f"→ Varianza Flesch-Kincaid: {varianzaFlesch:.2f}")
        print("\t","\t",f"→ Varianza Drive: {varianza:.2f}")
        print("\t","\t",f"→ Profundidad Arbol:",depth,"\n")

        print("3. ESTRUCTURA DE CONTENIDO:")
        print("\t",f"* Grado De Cumplimiento: ", num_secciones)
        titulos = extract_titles(pdf_path)
        imprimir_maxima_profundidad(titulos)
        print("\n")
        print("////////////////////////////////////////////////////////////////////")
        """
        
        #   /////////////////////////-- 3. REPRODUCIBILIDAD --///////////////////////////////////////
        """
        # Resultados PDF
        print(f"Documento: '{filename}':")
        print("ALGORITMO: ", SW_Algoritmo, "%", Total_Algoritmo)
        print("\t","* Repositorio: ", SW_A_Repo)
        print("\t","* Plataforma: ", SW_A_Plataforma)
        print("\t","* Sitio: ", SW_A_Sitio)
        print("\t","* Tipo Recurso: ",SW_A_Tipo_recurso)
        print("\t","* Tamaño Datos: ", SW_A_Tamaño_Datos)
        print("\t","* Licensia Uso: ", SW_Licencia_uso)
        print("\t","* Licencia Autorizacion: ", SW_Licencia_Autorizacion)
        print("\t","* Conjunto Datos: ", SW_A_Conjunto_datos)
        print("\t","* Formato Texto: ", SW_A_Formato_texto,"\n")


        print("ECUACIONES: ", SW_Ecuacion, "%", Total_Ecuaciones)
        print("\t","* Repositorio: ", SW_E_Repo)
        print("\t","* Plataforma: ", SW_E_Plataforma)
        print("\t","* Sitio: ", SW_E_Sitio)
        print("\t","* Tipo Recurso: ", SW_E_Tipo_recurso)
        print("\t","* Tamaño Datos: ", SW_E_Tamaño_Datos)
        print("\t","* Licensia Uso: ", SW_Licencia_uso)
        print("\t","* Licencia Autorizacion: ", SW_Licencia_Autorizacion)
        print("\t","* Conjunto Datos: ", SW_E_Conjunto_datos)
        print("\t","* Formato Texto: ", SW_E_Formato_texto,"\n")


        print("DATOS PROCESADOS: ",SW_Datos_Procesados, "%", Total_Datos_P)
        print("\t","* Repositorio: ", SW_P_Repo)
        print("\t","* Plataforma: ", SW_P_Plataforma)
        print("\t","* Sitio: ", SW_P_Sitio)
        print("\t","* Tipo de Recurso: ", SW_P_Tipo_recurso)
        print("\t","* Tamaño Datos: ", SW_P_Tamaño_Datos)
        print("\t","* Licensia Uso: ", SW_Licencia_uso)
        print("\t","* Licencia Autorizacion: ", SW_Licencia_Autorizacion)
        print("\t","* Conjunto Datos: ", SW_P_Conjunto_datos)
        print("\t","* Formato Texto: ", SW_P_Formato_texto,"\n")


        print("DATOS BRUTOS: ",SW_Datos_Brutos, "%", Total_Datos_B)
        print("\t","* Repositorio: ", SW_B_Repo)
        print("\t","* Plataforma: ", SW_B_Plataforma)
        print("\t","* Sitio: ", SW_B_Sitio)
        print("\t","* Tipo de Recurso: ", SW_B_Tipo_recurso)
        print("\t","* Tamaño Datos: ", SW_B_Tamaño_Datos)
        print("\t","* Licensia Uso: ", SW_Licencia_uso)
        print("\t","* Licencia Autorizacion: ", SW_Licencia_Autorizacion)
        print("\t","* Conjunto Datos: ", SW_B_Conjunto_datos)
        print("\t","* Formato Texto: ", SW_B_Formato_texto,"\n")
        """

        # Limpiar para el sig. archivo PDF
        url = ''
        urls = ''
        urls_encontrados = []
        urls_repositorio = []

        print("Articulo Numero ",archivo_num, "Procesado")
