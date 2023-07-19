from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date


def menu_update():
    today = date.today()
    day = today.strftime("%B %d, %Y")

    dining_halls = ["south-quad", "twigs-at-oxford", "north-quad", "mosher-jordan", "markley", "east-quad",
                    "bursley"]
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
                f.write(meal_name + " menu at " + hall + " on " + day + "\n")
                for item in items:
                    f.write(item.get_text() + "\n")

    f = open("closed-halls", "w", encoding="utf-8")
    for hall in not_serving:
        f.write(hall + "\n")


app = Flask(__name__)


@app.route('/bot', methods=['GET', 'POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    hall = "no hall"
    meal = "no meal"
    responded = False
    helpmsg = "Please enter the dining hall and the meal you want. Ex: \"South Quad Dinner\" " + "\n" + "Here is a list of dining halls: " + "\n" + "Bursley, East Quad, Markley, Mojo, North Quad, South Quad, Twigs"

    today = date.today()
    day = today.strftime("%B %d, %Y")

    with open('date', 'r') as f:
        data_date = f.readline()
        print(data_date)

    if data_date != day:
        with open('date', 'w', encoding="utf-8") as f:
            f.write(day)
        menu_update()

    if 'help' in incoming_msg:
        # return a quote

        msg.body(helpmsg)
        responded = True
    if 'bursley' in incoming_msg:
        hall = "bursley"
    elif 'east quad' in incoming_msg:
        hall = "east-quad"
    elif 'markley' in incoming_msg:
        hall = "markley"
    elif 'mojo' in incoming_msg:
        hall = "mosher-jordan"
    elif 'north quad' in incoming_msg:
        hall = "north-quad"
    elif 'south quad' in incoming_msg:
        hall = "south-quad"
    elif 'twigs' in incoming_msg:
        hall = "twigs-at-oxford"
    else:
        msg.body("Please respond with a valid hall. Text help for more details.")
        return str(resp)

    with open('closed-halls', 'r', encoding="utf-8") as f:
        closed_halls = set(line.strip() for line in f)

    if hall in closed_halls:
        msg.body(f"{hall} is not serving food today.")
        return str(resp)

    if 'breakfast' in incoming_msg:
        meal = "Breakfast"
    elif 'lunch' in incoming_msg:
        meal = "Lunch"
    elif 'brunch' in incoming_msg:
        meal = 'Brunch'
    elif 'dinner' in incoming_msg:
        meal = 'Dinner'
    else:
        msg.body("Please respond with a valid meal. Text help for more details.")
        return str(resp)

    try:
        with open(hall + '-' + meal, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        msg.body(f"{hall} is not serving {meal} today.")
        return str(resp)

    msg.body(data)

    return str(resp)


if __name__ == '__main__':
    app.run(debug=False)
