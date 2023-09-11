from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import logging

logger = logging.getLogger(__name__)

@cache_page(1 * 60)
def say_hello(request):
    try:
        logger.info('Calling httpbin')
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        logger.info('Response from httpbin')
    except requests.ConnectionError:
        logger.critical('httpbin is offine')
    return render(request, 'hello.html', {'name': 'Mosh'})
    
    # notify_customers.delay('Hello Mustafa')

    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails\hello.html',
    #         context= {'name': 'Mustafa'}
    #     )
    #     message.send(['arwa@musbuy.com'])
    #     # message = EmailMessage('subject', 'message', 'info@musbuy.com', ['arwa@musbuy.com'])
    #     # message.attach_file('playground\static\images\DSCN5531.jpg')
    #     # message.send()
    # except BadHeaderError:
    #     pass
