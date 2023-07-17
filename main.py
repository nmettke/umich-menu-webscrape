from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date

if __name__ == '__main__':
    # Date information
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    fname = "south_quad.txt"
    url = "https://dining.umich.edu/menus-locations/dining-halls/south-quad/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find('div', {'id': 'mdining-items'})
    meal_items = div.find_all('div', class_='courses')

    f = open(fname, "w", encoding="utf-8")
    f.write("Michigan Dining menu for " + d2 + "\n")
    for tag in meal_items:
        meal = tag.find_previous_sibling('h3')
        items = tag.find_all('div', class_='item-name')
        meal_name = meal.get_text()
        f.write(meal_name + "\n")
        for item in items:
            f.write(item.get_text() + "\n")





