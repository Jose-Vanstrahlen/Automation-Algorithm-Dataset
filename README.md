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
. from webdriver_manager.chrome import ChromeDriverManager.
. driver_path = ChromeDriverManager().install().

-----------------
ABOUT SELENIUM.
Selenium Installation:
install selenium using pip:
pip install selenium.

Download the browser controller (driver):
Selenium requires a specific controller to interact with the browser you want to automate. The driver is different for each browser.
For Chrome, you will need to download the ChromeDriver driver. Make sure to download the version compatible with your version of Chrome from the following link: 
https://sites.google.com/a/chromium.org/chromedriver/downloads

For Firefox, you will need to download the GeckoDriver driver. You can get it from the following link: https://github.com/mozilla/geckodriver/releases
Be sure to download the driver for the operating system you are using.

Configure the controller in the PATH:
After downloading the driver, you must add it to the system PATH or specify the path to the driver in your script.
If you are using Windows, you can place the driver file in an accessible location and add that location to the system PATH. This will allow Selenium to find the controller without specifying the full path in your script.
If you are using Linux or macOS, you can place the driver in an accessible location and add that location to the PATH. Alternatively, you can also specify the full path to the controller in your script.

Import Selenium into your Python script:
Once you've installed Selenium and configured the driver, you need to import the library into your Python script:
from selenium import webdriver

______________________________________________________________________________________________________________________________________
# About the Code:
In line #73, you must place the directory of articles to analyze (PDF) "dir_path = "user/your_directory""
In line #79, the list called "DoiDocs", you must place the DOIS of the articles to be analyzed.
Note the numerical prioritization order in python, the DOIS placed in the list must match the PDFs stored in your directory.

The results are exported to an excel file which you must choose its path, you can find this in the lines:
Line #2401, "with pd.ExcelFile("the route you want/RESULTS.xlsx", engine="openpyxl") as xls:"
Line #2422, "writer = pd.ExcelWriter("the route you want/RESULTS.xlsx", engine="openpyxl")"



