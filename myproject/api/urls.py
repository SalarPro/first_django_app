from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.getData ),
    path('new', views.new_post),
]
