from django.db.models import Sum

from geoTest.celery import app

from .models import Client


@app.task
def check_1000(client_id):
    user = Client.objects.get(id=client_id)
    if user.balance >= 1000:
        res = f'{user} balance > 1000'
        return print(res)


@app.task
def check_0(client_id):
    user = Client.objects.get(id=client_id)
    if user.balance <= 0:
        res = f'{user} balance < 0'
        return print(res)


@app.task
def check_100k(amount):
    if amount >= 100000:
        res = 'summary balance > 100k'
        return print(res)


@app.task
def check_amount():
    amount = Client.objects.aggregate(summary_balance=Sum('balance'))['summary_balance']
    check_100k.delay(amount)
    res = f'Summary balance = {amount}'
    return print(res)
