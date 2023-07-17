from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date

if __name__ == '__main__':
    # Date information
    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    dining_halls = ["south-quad", "twigs-at-oxford", "north-quad", "mosher-jordan", "markley", "east-quad", "bursley"]
    not_serving = set()
    url = "https://dining.umich.edu/menus-locations/dining-halls/"
    for hall in dining_halls:
        page = urlopen(url + hall)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        div = soup.find('div', {'id': 'mdining-items'})
        no_menu = div.find('p', class_='no-menu')
        if no_menu is not None:
            not_serving.add(hall)
            continue
        else:
            meal_items = div.find_all('div', class_='courses')
            for tag in meal_items:
                meal = tag.find_previous_sibling('h3')
                items = tag.find_all('div', class_='item-name')
                meal_name = meal.get_text()[1:]
                fname = hall + '-' + meal_name
                f = open(fname, "w", encoding="utf-8")
                f.write(meal_name + " menu at " + hall + " on " + d2 + "\n")
                for item in items:
                    f.write(item.get_text() + "\n")

    f = open("closed-halls", "w", encoding="utf-8")
    for hall in not_serving:
        f.write(hall + "\n")






