from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('new', views.new_post),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
