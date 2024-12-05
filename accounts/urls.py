from django.urls import path
from portfolio.views import project_list # importing the views from projects/portfoli
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('portfolio/', project_list , name ="portfolioapp"),# urls to projects after login
]