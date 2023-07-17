import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
myemail = "webscraper936@gmail.com"
mypassword = "ywterjjwocllpkye"
server.login(myemail, mypassword)

# Craft message (note: '\n' denotes line breaks)
message = 'Subject: {}\n\n{}'.format('', 'ready for me to carry you in league?')

nate = "9174066741"
annie = "2484137211"
chance = "7342318482"

verizon = "@vtext.com"
sprint = "@messaging.sprintpcs.com"

server.sendmail(myemail, nate + verizon, message)
server.quit()