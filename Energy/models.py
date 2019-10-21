from django.db import models

# Create your models here.
class Renewable_TotalMarketed_LowGrowth (models.Model):
  name = models.TextField()
  units = models.TextField()
  description = models.TextField()
  updated = models.TextField()
  
  def __str__(self):
    return self.name
  
class Data (models.Model):
  year = models.TextField()
  quads = models.IntegerField()
  renewable_totalmarketed_lowgrowth = models.ForeignKey( Renewable_TotalMarketed_LowGrowth, on_delete=models.CASCADE, related_name='data' )