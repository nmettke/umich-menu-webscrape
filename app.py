from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

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

    print(incoming_msg)

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

    with open(hall + '-' + meal, 'r') as file:
        data = file.read()

    msg.body(data)

    return str(resp)


if __name__ == '__main__':
    app.run(debug=False)
