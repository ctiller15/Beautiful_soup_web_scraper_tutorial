import requests
from bs4 import BeautifulSoup
import pprint

URL = 'https://www.monster.com/jobs/search/?q=Python-Developer&where=Tampa__2C-FL'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
print(results.prettify())
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(page.content)
