from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import twilio

if '__main__':
    # Date information
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    url = "https://dining.umich.edu/menus-locations/dining-halls/south-quad/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    fname = "south_quad.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
