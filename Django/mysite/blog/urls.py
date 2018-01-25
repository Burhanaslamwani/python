from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:heading_id>/', views.detail, name='detail'),
    path('ajx/', views.ajx, name='ajx'),
    path('flight/', views.flight, name='flight')

]
