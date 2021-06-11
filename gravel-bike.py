import requests
from bs4 import BeautifulSoup
import os
import time
from twilio.rest import Client

SEVEN_URL = "https://www.canyon.com/en-us/grizl-cf-sl-7/2848.html"
EIGHT_URL = "https://www.canyon.com/en-us/grizl-cf-sl-8/2850.html"

TWILIO_NUM='+16573013195'
MY_PHONE=os.environ['MY_PHONE'] # export MY_PHONE='+18001234567'

# size xs bike
SELECTOR = "#js-productsummary > div.productDescription__productSummary.xlt-pdpContent > div.productDescription__variationAttributeWrapper > div.productConfiguration.js-productConfiguration.productConfiguration--size.xlt-pdpVariations > ul > li:nth-child(2) > div"

# size s bike
SMALL_SELECTOR = "#js-productsummary > div.productDescription__productSummary.xlt-pdpContent > div.productDescription__variationAttributeWrapper > div.productConfiguration.js-productConfiguration.productConfiguration--size.xlt-pdpVariations > ul > li:nth-child(3) > div"

def app():
    page_7 = requests.get(SEVEN_URL)
    page_8 = requests.get(EIGHT_URL)

    soup_7 = BeautifulSoup(page_7.content, 'html.parser')
    small_bike_7 = soup_7.select(SMALL_SELECTOR)

    soup_8 = BeautifulSoup(page_8.content, 'html.parser')
    small_bike_8 = soup_8.select(SMALL_SELECTOR)

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)


    nobike=True 
    num_checks = 0
    while nobike:
        print("checking")
        time.sleep(60*20) 

        if "Coming soon" in str(small_bike_8):
            print("still coming soon")
            if num_checks < 4 or num_checks % (24*3) == 10:
                message = client.messages \
                        .create(
                                body=f"Grizl 8 still not available, check number {num_checks}",
                                from_=TWILIO_NUM,
                                to=MY_PHONE
                                )
        else:
            nobike=False
            message = client.messages \
                    .create(
                            body="grizl 8 AVAILABLE!!!!",
                            from_=TWILIO_NUM,
                            to=MY_PHONE
                            )
        num_checks+=1

if __name__ == "__main__":
    app()


