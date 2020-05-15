from django.urls import path, re_path
from PortfolioApp import views

urlpatterns = [
    path('', views.render_home_page, name='home_page'),
]
