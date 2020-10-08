from bs4 import BeautifulSoup as Bs
import requests
from django import template


register = template.Library()


@register.filter()
def usd_price(value):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/85.0.4183.83 Safari/537.36'}

    response = requests.get('https://cbr.ru/', headers=headers)

    soup = Bs(response.text, 'html.parser')

    price = soup.find('div', class_='indicator_el_value mono-num').get_text()
    price_usd = value / float(price[:-1].replace(',', '.'))

    return f'{price_usd:.3f}'
