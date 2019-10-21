from django.shortcuts import render
import requests

r = requests.get('https://api.eia.gov/series/?api_key=8e1ad445c4f1cf0f695f035004b477b0&series_id=AEO.2019.LOWMACRO.CNSM_NA_NA_NA_NA_NA_NA_QBTU.A')
r.json()
# Create your views here.
