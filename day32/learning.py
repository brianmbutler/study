import smtplib
import datetime as dt
import random

my_email = 'trtltrtlgame@gmail.com'
today = dt.datetime.now().weekday()

if today == 5:
    with open('./day32/quotes.txt') as f:
        quotes = f.read().splitlines()
        selected_quote = random.choice(quotes)
            
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='trtltrtlgame@gmail.com', password='ENTER_APP_PASSWORD')
        connection.sendmail(
                from_addr='trtlgame@gmail.com', 
                to_addrs='trtltrtlgame@gmail.com', 
                msg=f'Subject:Hello\n\nHere is your motivational quote:\n {selected_quote}')
        connection.close
