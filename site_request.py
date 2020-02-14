import requests
import pprint

URL = 'https://www.monster.com/jobs/search/?q=Python-Developer&where=Tampa__2C-FL'
page = requests.get(URL)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(page.content)
