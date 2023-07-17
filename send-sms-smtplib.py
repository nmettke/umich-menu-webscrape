import smtplib

if __name__ == '__main__':
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    myemail = "webscraper936@gmail.com"
    mypassword = "ywterjjwocllpkye"
    server.login(myemail, mypassword)

    # Craft message (note: '\n' denotes line breaks )
    fname = 'south_quad.txt'
    with open(fname, 'r') as file:
        message = file.read()

    # message = 'Subject: {}\n\n{}'.format('', '')

    nate = "9174066741"
    annie = "2484137211"
    chance = "7342318482"

    verizon = "@vtext.com"
    sprint = "@messaging.sprintpcs.com"
    mint = "@tmomail.net"

    server.sendmail(myemail, nate + verizon, message)
    server.quit()
