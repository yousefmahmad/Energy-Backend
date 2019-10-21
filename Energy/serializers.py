from rest_framework import serializers
from .models import Renewable_TotalMarketed_LowGrowth, Data

class Renewable_TotalMarketed_LowGrowth_Serializer(serializers.ModleSerializer):
  data = DataSerializer(many=True)
  class Meta:
    model = Renewable_TotalMarketed_LowGrowth
    fields = ('name', 'units', 'description', 'updated')
    
class DataSerializer(serializers.ModelSerializer)
  class Meta:
    model = Data
    fields = ('year', 'quads')