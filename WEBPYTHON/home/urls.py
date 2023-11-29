from django.urls import path
from.import views
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('cv/', views.base1),
    path('tintuc/', views.tintuc),

   path('register/', views.register, name="register"),
#    path('login/',auth_views.login,{'template_name':'pages/login.html'}, name="login"),
   path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
   
   path('logout/',LogoutView.as_view(next_page='/'),name='logout'),



]