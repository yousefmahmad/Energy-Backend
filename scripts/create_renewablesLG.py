import json
import requests
fixtures = []

renewablesLG = requests.get('https://api.eia.gov/series/?api_key=8e1ad445c4f1cf0f695f035004b477b0&series_id=AEO.2019.LOWMACRO.CNSM_NA_NA_NA_NA_NA_NA_QBTU.A')

with open('renewablesLG','r') as file:
  renewable = json.load(file)
  
for pk, renewables in enumeerate(renewable, start=1):
  fixture = {
    "model": 'Renewable_TotalMarketed_LowGrowth',
    "pk":"pk",
    "fields": renewables
  }
  
  fixtures.append(fixture)
  
with open('../fixtures/renewablesLG.json', 'w') as of:
  json.dumb(fixtures, of, indent=4)