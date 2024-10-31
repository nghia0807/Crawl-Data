from django.shortcuts import render
import requests
# Create your views here.

def coin_list(request):
    coin_url = 'https://apiforlearning.zendvn.com/api/get-coin'
    coin_respond = requests.get(coin_url, verify=False)
    items_coin = coin_respond.json()

    return render(request, 'coin.html', {"items_coin": items_coin})

def gold_list(request):
    gold_url = 'https://apiforlearning.zendvn.com/api/get-gold'
    gold_respond = requests.get(gold_url, verify=False)
    items_gold = gold_respond.json()

    return render(request, 'gold.html', {"items_gold": items_gold})