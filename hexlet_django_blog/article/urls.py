from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('<str:tags>/<int:article_id>/', views.index, name='article'),
]
