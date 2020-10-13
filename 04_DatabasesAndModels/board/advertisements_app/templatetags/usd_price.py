from datetime import datetime

import requests
from bs4 import BeautifulSoup as Bs

from django import template


register = template.Library()


@register.filter()
def usd_price(value):

    time = datetime.now()

    response = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={time.day}/{time.month}/{time.year}')

    soup = Bs(response.text, 'html.parser')

    price = soup.find(id='R01235').get_text()[-7:]
    price_usd = value / float(price.replace(',', '.'))

    return f'{price_usd:.3f}'
