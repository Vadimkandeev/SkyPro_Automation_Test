from classes import Mailing
from classes import Adress

myMailing_To = Adress("45678925", "Samara", "Aurora", "157", "63")
myMailing_From = Adress("95621123", "Moscow", "Mira", "25", "8")
myMailing = Mailing(myMailing_To, myMailing_From, 1200, "RU123456")

print("Отправление ",myMailing.track, "из ",  myMailing_From.city, myMailing_From.street, myMailing_From.house,"- ",  myMailing_From.apartment, "В ", myMailing_To.city, myMailing_To.street, myMailing_To.house,"-", myMailing_To.apartment, ". ", "Стоимость ", myMailing.cost, " рублей")