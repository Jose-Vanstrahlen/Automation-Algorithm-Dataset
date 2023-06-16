# Automation-Algorithm-Dataset
______________________________________________________________________________________________________________________________________

This algorithm has the function of automatically determining 3 evaluation and analysis metrics for any scientific article in English, in PDF format. It can be from 1 single item to the amount you want. (Taking into account the limitations of the apis of the databases to use). The results are exported to an excel which shows in detail the value of each metric and its respective elements found.

The 3 metrics that are evaluated are:
visibility.
understandability.
reproducibility.

Different technologies were implemented such as; Web Scraping, Natural Language Processing. Analysis of data,


# *** LIBRARIES ***

Python standard libraries.
No additional installation required, included in the standard Python installation:

os
string
json
requests
re
mimetypes
urllib.request
ast
xml.etree.ElementTree


Installation of the libraries
To use the algorithm install the following libraries:

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
. Download and install the "en_core_web_sm" language model:
. python -m spacy download en_core_web_sm


. nltk
. pip install nltk
Resources needed for nltk:
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
nltk.download('large_grammars')
nltk.download('cmudict')
nltk.download('wordnet')


. selenium
. pip install selenium
Install Chrome WebDriver and the PATH on your system:
. from webdriver_manager.chrome import ChromeDriverManager
. driver_path = ChromeDriverManager().install()


______________________________________________________________________________________________________________________________________
# About the Code:
In line #73, you must place the directory of articles to analyze (PDF) "dir_path = "user/your_directory""
In line #79, the list called "DoiDocs", you must place the DOIS of the articles to be analyzed.
Note the numerical prioritization order in python, the DOIS placed in the list must match the PDFs stored in your directory.

The results are exported to an excel file which you must choose its path, you can find this in the lines:
Line #2401, "with pd.ExcelFile("the route you want/RESULTS.xlsx", engine="openpyxl") as xls:"
Line #2422, "writer = pd.ExcelWriter("the route you want/RESULTS.xlsx", engine="openpyxl")"



