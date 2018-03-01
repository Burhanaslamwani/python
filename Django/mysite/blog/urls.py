from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:heading_id>/', views.detail, name='detail'),
    path('ajx/', views.ajx, name='ajx'),
    path('flight/', views.flight, name='flight'),
    # path('index2/', views.login, name='login'),
    path('flightrate/', views.flightrate, name='flightrate'),
    path('news/', views.news, name='news'),
    path('login/',login, {'template_name':'blog/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout')
]
