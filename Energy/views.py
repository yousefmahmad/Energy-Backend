from rest_framework import generics
from .serializers import Renewable_TotalMarketed_LowGrowth_Serializer, DataSerializer
from .models import Renewable_TotalMarketed_LowGrowth, Data


# Create your views here.
class Renewable_TotalMarketed_LowGrowth_List(generics.ListCreateAPIView):
  queryset = Renewable_TotalMarketed_LowGrowth.objects.all()
  serializer_class = Renewable_TotalMarketed_LowGrowth_Serializer

class Renewable_TotalMarketed_LowGrowth_Detail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Renewable_TotalMarketed_LowGrowth.objects.all()
  serializer_class = Renewable_TotalMarketed_LowGrowth_Serializer