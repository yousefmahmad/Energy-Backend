import requests
from rest_framework import generics
from .serializers import Renewable_TotalMarketed_LowGrowth_Serializer, DataSerializer
from .models import Renewable_TotalMarketed_LowGrowth, Data


r = requests.get('https://api.eia.gov/series/?api_key=8e1ad445c4f1cf0f695f035004b477b0&series_id=AEO.2019.LOWMACRO.CNSM_NA_NA_NA_NA_NA_NA_QBTU.A')
r.json()
# Create your views here.
class Renewable_TotalMarketed_LowGrowth_List(generics.ListCreateAPIView):
  queryset = Renewable_TotalMarketed_LowGrowth.objects.all()
  serializer_class = Renewable_TotalMarketed_LowGrowth_Serializer

class Renewable_TotalMarketed_LowGrowth_Detail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Renewable_TotalMarketed_LowGrowth.objects.all()
  serializer_class = Renewable_TotalMarketed_LowGrowth_Serializer