from rest_framework import serializers
from .models import Renewable_TotalMarketed_LowGrowth, Data


class DataSerializer(serializers.ModelSerializer):
  class Meta:
    model = Data
    fields = ('year', 'quads')

class Renewable_TotalMarketed_LowGrowth_Serializer(serializers.ModelSerializer):
  data = DataSerializer(many=True)
  class Meta:
    model = Renewable_TotalMarketed_LowGrowth
    fields = ('name', 'units', 'description', 'updated', 'data')
    
