from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
   path('Renewable_TotalMarketed_LowGrowth', views.Renewable_TotalMarketed_LowGrowth_List.as_view(), name='Renewable_TotalMarketed_LowGrowth_list'),
    path('Renewable_TotalMarketed_LowGrowth/<int:pk>', views.Renewable_TotalMarketed_LowGrowth_Detail.as_view(), name='Renewable_TotalMarketed_LowGrowth_detail')
]