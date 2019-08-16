import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_3?keywords=python&qid=1565977020&s=gateway&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.377.100 Safari/537.36'}
}

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('vpathalam@gmail.com', 'mjutimzlroarivxo')

    subject = 'Price decreased for the item'
    body = 'check the amazonlink: https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_3?keywords=python&qid=1565977020&s=gateway&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('vpathalam@gmail.com', 'test@gmail.com', msg)
    print('email has been successfully sent!')

    server.quit()

def checkPrice():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find()id="priceblock_ourprice").get_text()
    convertedPrice = float(price[0:5])


    if(convertedPrice < 16.00):
        sendEmail()

while(True):=
    checkPrice()
    time.sleep(60 * 60)
