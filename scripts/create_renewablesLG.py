import json
import requests
fixtures = []

renewablesLG = requests.get('https://api.eia.gov/series/?api_key=8e1ad445c4f1cf0f695f035004b477b0&series_id=AEO.2019.LOWMACRO.CNSM_NA_NA_NA_NA_NA_NA_QBTU.A')
renewablesLG = renewablesLG.json()
print(renewablesLG['series'][0])
  

  
#   fixtures.append(fixture)
  
# with open('../fixtures/renewablesLG.json', 'w') as of:
#   json.dumb(fixtures, of, indent=4)