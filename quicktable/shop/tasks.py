import logging
import pprint
import requests
from bs4  import BeautifulSoup

from rest_framework.exceptions import APIException

# from celery import shared_task
from quicktable.celery import app

logger = logging.getLogger('django')

@app.task
def collect_shop_info():
    try:
        response = requests.get('google.com')
        soup = BeautifulSoup(response.text, 'html.parser')
        shop = soup.find_all('div', class_='z3HNkc')
        pprint.pprint(shop)
        
    except APIException as exe:
        raise APIException(exe.detail)


