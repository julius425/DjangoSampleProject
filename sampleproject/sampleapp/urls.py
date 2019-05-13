from django.urls import path
from . import views


app_name = 'sampleapp'

urlpatterns = [
    path('', views.model_list_view, name='model_list'),
    path('models/<model_id>/', views.model_detail_view, name='model_detail'),
]
