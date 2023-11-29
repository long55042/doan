from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('<int:id>/', views.post),
    # path('<int:title>/', views.post)
]
