import time
import json
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from currency_exchange.settings import API_KEY

exchange_rates = []


@csrf_exempt
@require_http_methods(["GET"])
def get_current_usd(request):
    global exchange_rates
    
    api_url = f"https://api.currencyapi.com/v3/latest?apikey={API_KEY}&currencies=RUB"
    response = requests.get(api_url)
    data = response.json()
    
    value = data['data']['RUB']['value']

    exchange_rates.append(value)
    exchange_rates = exchange_rates[-10:]  

    time.sleep(10)

    return JsonResponse({
        'current_usd_to_rub': value,
        'last_10_requests': exchange_rates,
    })
